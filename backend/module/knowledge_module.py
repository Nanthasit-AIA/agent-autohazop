import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List

from decorators import logger


MAX_GENERATION_KNOWLEDGE_CHARS = int(os.getenv("HAZOP_GENERATION_KNOWLEDGE_CHARS", "18000"))
MAX_MANDATORY_GENERATION_KNOWLEDGE_CHARS = int(os.getenv("HAZOP_MANDATORY_GENERATION_KNOWLEDGE_CHARS", "14500"))
MAX_MANDATORY_GENERATION_SOURCE_CHARS = int(os.getenv("HAZOP_MANDATORY_GENERATION_SOURCE_CHARS", "1900"))
MAX_SECTION_CHARS = 2400

MANDATORY_GENERATION_SOURCE_PRIORITY = (
    "backend/skill.md",
    "autohazop-agent-pack/skill.md",
    "references/workflows/scgc-hazop-lopa-generation-method.md",
    "references/workflows/pfd-pid-tracing.md",
    "book-instrumentation-control-systems-documentation/skill.md",
    "book-instrumentation-control-systems-documentation/references/hazop-control-document-qa.md",
    "book-instrumentation-control-systems-documentation/references/pid-loop-logic-checklist.md",
    "control-loop-layer-extractor/skill.md",
    "control-loop-layer-extractor/references/extraction-workflow.md",
    "control-loop-layer-extractor/references/hazop-integration.md",
    "references/workflows/cause-consequence.md",
    "references/workflows/severity-assessment.md",
    "references/workflows/lopa-ipl-assessment.md",
    "references/workflows/risk-ranking.md",
)

MANDATORY_BACKEND_HEADINGS = {
    "Team Working Style",
    "SCGC Procedure Overlay For Generation",
    "PFD/P&ID Reading Requirements",
    "Parameters And Guide Words",
    "Cause Rules",
    "Consequence Rules",
    "Severity Rule",
    "Initial And Final Risk",
    "IPL Handling",
    "Review Before Finalizing",
}

MANDATORY_AUTOHAZOP_HEADINGS = {
    "Core Rule",
    "Mandatory Analysis Contract",
    "Foundation Behavior",
    "Execution Flow",
    "Context Extraction Schema",
    "Quality Rules",
}


def _project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _safe_relative(path: Path) -> str:
    try:
        return str(path.relative_to(_project_root()))
    except ValueError:
        return str(path)


def _normalized_source(source: str) -> str:
    return str(source or "").replace("\\", "/").lower()


def _base_heading(heading: str) -> str:
    return re.sub(r"\s+\(part\s+\d+\)$", "", str(heading or "")).strip()


def _format_knowledge_block(item: Dict[str, Any]) -> str:
    return (
        f"SOURCE: {item['source']}\n"
        f"HEADING: {item['heading']}\n"
        f"{item['text'].strip()}"
    ).strip()


def _mandatory_generation_priority(source: str) -> int:
    source_lower = _normalized_source(source)
    for idx, key in enumerate(MANDATORY_GENERATION_SOURCE_PRIORITY):
        if key in source_lower:
            return idx
    return len(MANDATORY_GENERATION_SOURCE_PRIORITY)


def _is_mandatory_generation_section(section: Dict[str, str]) -> bool:
    source = _normalized_source(section.get("source", ""))
    heading = _base_heading(section.get("heading", ""))

    if source == "backend/skill.md":
        return heading in MANDATORY_BACKEND_HEADINGS

    if source.endswith("autohazop-agent-pack/skill.md"):
        return heading in MANDATORY_AUTOHAZOP_HEADINGS

    return any(key in source for key in MANDATORY_GENERATION_SOURCE_PRIORITY[2:])


def _read_text(path: Path, max_chars: int = 90000) -> str:
    try:
        return path.read_text(encoding="utf-8-sig", errors="replace")[:max_chars]
    except Exception as exc:
        logger.warning("Failed to read knowledge file %s: %s", path, exc)
        return ""


def _knowledge_paths() -> List[Path]:
    root = _project_root()
    paths: List[Path] = []

    primary = root / "backend" / "Skill.md"
    if primary.exists():
        paths.append(primary)

    skills_dir = root / "skills"
    if skills_dir.exists():
        paths.extend(sorted(skills_dir.glob("*/SKILL.md")))
        paths.extend(sorted(skills_dir.glob("*/Skill.md")))
        paths.extend(sorted(skills_dir.glob("*/references/**/*.md")))

    seen = set()
    unique_paths: List[Path] = []
    for path in paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_paths.append(path)

    return unique_paths


def _split_markdown_sections(path: Path, text: str) -> List[Dict[str, str]]:
    sections: List[Dict[str, str]] = []
    matches = list(re.finditer(r"(?m)^#{1,3}\s+.+$", text))

    if not matches:
        stripped = text.strip()
        if stripped:
            sections.append(
                {
                    "source": _safe_relative(path),
                    "heading": path.name,
                    "text": stripped[:MAX_SECTION_CHARS],
                }
            )
        return sections

    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        heading = match.group(0).lstrip("#").strip()
        chunk = text[start:end].strip()
        if not chunk:
            continue

        paragraphs = re.split(r"\n\s*\n", chunk)
        current = ""
        part = 1
        for paragraph in paragraphs:
            if len(current) + len(paragraph) + 2 > MAX_SECTION_CHARS and current:
                sections.append(
                    {
                        "source": _safe_relative(path),
                        "heading": f"{heading} (part {part})" if part > 1 else heading,
                        "text": current.strip(),
                    }
                )
                current = ""
                part += 1
            current += paragraph + "\n\n"

        if current.strip():
            sections.append(
                {
                    "source": _safe_relative(path),
                    "heading": f"{heading} (part {part})" if part > 1 else heading,
                    "text": current.strip()[:MAX_SECTION_CHARS],
                }
            )

    return sections


@lru_cache(maxsize=1)
def _knowledge_sections() -> List[Dict[str, str]]:
    sections: List[Dict[str, str]] = []
    for path in _knowledge_paths():
        text = _read_text(path)
        if text:
            sections.extend(_split_markdown_sections(path, text))
    return sections


def _tokenize(text: str) -> List[str]:
    stopwords = {
        "the",
        "and",
        "for",
        "with",
        "this",
        "that",
        "from",
        "into",
        "when",
        "then",
        "line",
        "node",
        "process",
        "description",
    }
    tokens: List[str] = []
    seen = set()
    for token in re.findall(r"[A-Za-z0-9_./&+-]{2,}", text or ""):
        lowered = token.lower()
        if lowered in stopwords or lowered in seen:
            continue
        seen.add(lowered)
        tokens.append(lowered)
    return tokens


def _domain_expansion(parameter: str, guide_word: str, raw_query: str) -> str:
    text = f"{parameter} {guide_word} {raw_query}".lower()
    terms = [
        "hazop",
        "deviation",
        "cause",
        "consequence",
        "safeguard",
        "recommendation",
        "lopa",
        "ipl",
        "risk matrix",
    ]

    if "pressure" in text or "overpressure" in text or "psv" in text or "relief" in text:
        terms.extend(["pressure relief", "overpressure", "psv", "rupture disk", "flare", "effluent", "blocked outlet"])
    if "flow" in text or "pump" in text or "valve" in text:
        terms.extend(["pump", "valve", "blockage", "reverse flow", "minimum flow", "cavitation", "check valve"])
    if "temperature" in text or "cooling" in text or "heating" in text:
        terms.extend(["temperature", "cooling failure", "heating", "runaway", "fire", "thermal"])
    if "level" in text or "tank" in text or "vessel" in text:
        terms.extend(["tank", "vessel", "overfill", "low level", "dry running", "venting", "blanketing"])
    if "composition" in text or "phase" in text or "concentration" in text:
        terms.extend(["contamination", "off-spec", "chemical release", "dispersion", "flammable", "toxic"])
    if "instrument" in text or "alarm" in text or "operator" in text:
        terms.extend(["alarm management", "operator response", "bpcs", "interlock", "sis", "sif"])
    if any(term in text for term in ("control", "controller", "loop", "pv", "sp", "mv", "final element", "fcv", "pcv", "lcv", "tcv")):
        terms.extend([
            "control loop",
            "pv sp mv",
            "controller",
            "final element",
            "manipulated variable",
            "controlled asset",
            "signal path",
            "loop diagram",
            "control narrative",
        ])
    if "maintenance" in text or "operation" in text or "human" in text:
        terms.extend(["human factors", "operating procedure", "maintenance", "moc", "incident learning"])
    if "security" in text:
        terms.extend(["security vulnerability", "sva", "intentional event"])

    return " ".join(terms)


def _path_boost(source: str, query_text: str) -> int:
    source_lower = source.lower()
    query_lower = query_text.lower()
    boost = 0
    if "scgc-hazop-lopa-generation-method" in source_lower:
        boost += 18
    if "instrumentation-control-systems-documentation" in source_lower and any(
        term in query_lower
        for term in (
            "instrument",
            "tag",
            "loop",
            "alarm",
            "interlock",
            "logic",
            "cause-and-effect",
            "control",
            "p&id",
            "pid",
            "shutdown",
            "trip",
            "xv",
            "pt",
            "ft",
            "lt",
            "tt",
        )
    ):
        boost += 24
    if "control-loop-layer-extractor" in source_lower and any(
        term in query_lower
        for term in (
            "control",
            "controller",
            "loop",
            "pv",
            "sp",
            "mv",
            "final element",
            "manipulated variable",
            "controlled asset",
            "signal path",
            "loop diagram",
            "control narrative",
            "fic",
            "pic",
            "lic",
            "tic",
            "fcv",
            "pcv",
            "lcv",
            "tcv",
        )
    ):
        boost += 26
    pairs = [
        ("instrumentation", ["instrument", "tag", "loop", "alarm", "interlock", "logic", "control", "p&id"]),
        ("control-loop", ["control", "controller", "loop", "pv", "sp", "mv", "final", "element"]),
        ("lopa", ["lopa", "ipl", "initiating", "conditional", "sil"]),
        ("sis", ["sis", "sif", "sil", "proof", "instrument"]),
        ("relief", ["relief", "psv", "pressure", "flare", "fire", "explosion", "consequence"]),
        ("alarm", ["alarm", "operator", "instrument"]),
        ("moc", ["moc", "change", "procedure", "maintenance"]),
        ("documentation", ["documentation", "records", "audit"]),
        ("human", ["human", "operator", "incident"]),
        ("reliability", ["failure", "reliability", "pfd", "rate"]),
        ("hazop", ["hazop", "guide", "deviation", "node"]),
        ("risk", ["risk", "qra", "criteria", "matrix"]),
    ]
    for source_key, terms in pairs:
        if source_key in source_lower and any(term in query_lower for term in terms):
            boost += 10
    for term in _tokenize(query_text):
        if len(term) >= 3 and term in source_lower:
            boost += 4
    if "book-wiki" in source_lower:
        boost += 2
    if "\\book-" in source_lower or "/book-" in source_lower:
        boost += 2
    return boost


def build_generation_knowledge_context(selection_context: Dict[str, Any]) -> str:
    parameter = str(selection_context.get("parameter") or "")
    guide_word = str(selection_context.get("guide_word") or "")
    raw_query = " ".join(
        str(selection_context.get(key) or "")
        for key in (
            "line_id",
            "node",
            "valves",
            "instruments",
            "context",
            "process_description",
        )
    )
    expanded_query = f"{raw_query} {parameter} {guide_word} {_domain_expansion(parameter, guide_word, raw_query)}"
    query_terms = _tokenize(expanded_query)

    scored: List[Dict[str, Any]] = []
    for section in _knowledge_sections():
        haystack = f"{section['source']}\n{section['heading']}\n{section['text']}".lower()
        score = _path_boost(section["source"], expanded_query)
        heading = section["heading"].lower()
        for term in query_terms:
            if term in haystack:
                score += 3 if term in heading else 1
        if score > 0:
            scored.append({**section, "score": score})

    scored.sort(key=lambda item: item["score"], reverse=True)

    selected: List[str] = [
        (
            "MANDATORY GENERATION SKILL BUNDLE ACTIVE\n"
            "Use these loaded HAZOP/LOPA skills as required reasoning gates before generating rows: "
            "SCGC method, PFD/P&ID tracing, instrument/control documentation QA, "
            "control-loop layer extraction, cause-consequence credibility, severity assessment, LOPA/IPL assessment, "
            "risk ranking, recommendation QA, and scenario-specific references."
        )
    ]
    used_chars = len(selected[0]) + 2
    selected_keys = set()

    mandatory_sections = [
        section for section in _knowledge_sections() if _is_mandatory_generation_section(section)
    ]
    mandatory_sections.sort(
        key=lambda item: (
            _mandatory_generation_priority(item["source"]),
            _base_heading(item["heading"]),
        )
    )

    mandatory_budget = min(
        MAX_MANDATORY_GENERATION_KNOWLEDGE_CHARS,
        max(0, MAX_GENERATION_KNOWLEDGE_CHARS - 1800),
    )
    mandatory_source_chars: Dict[str, int] = {}
    for item in mandatory_sections:
        source_key = _normalized_source(item["source"])
        source_used = mandatory_source_chars.get(source_key, 0)
        if source_used >= MAX_MANDATORY_GENERATION_SOURCE_CHARS:
            continue

        block = _format_knowledge_block(item)
        key = (item["source"], item["heading"])
        if key in selected_keys:
            continue

        source_remaining = MAX_MANDATORY_GENERATION_SOURCE_CHARS - source_used
        if len(block) > source_remaining:
            if source_remaining < 600:
                continue
            block = block[:source_remaining].rsplit("\n", 1)[0].strip()

        if used_chars + len(block) + 2 > mandatory_budget:
            remaining = mandatory_budget - used_chars - 2
            if remaining < 700:
                break
            block = block[:remaining].rsplit("\n", 1)[0].strip()
        selected.append(block)
        selected_keys.add(key)
        used_chars += len(block) + 2
        mandatory_source_chars[source_key] = source_used + len(block) + 2
        if used_chars >= mandatory_budget:
            break

    for item in scored[:16]:
        key = (item["source"], item["heading"])
        if key in selected_keys:
            continue
        block = _format_knowledge_block(item)
        if used_chars + len(block) + 2 > MAX_GENERATION_KNOWLEDGE_CHARS:
            remaining = MAX_GENERATION_KNOWLEDGE_CHARS - used_chars - 2
            if remaining < 900:
                break
            block = block[:remaining].rsplit("\n", 1)[0].strip()
        selected.append(block)
        selected_keys.add(key)
        used_chars += len(block) + 2
        if used_chars >= MAX_GENERATION_KNOWLEDGE_CHARS:
            break

    if not selected:
        return "No source-derived skill/wiki context matched this selection. Use the core HAZOP prompt and mark missing basis explicitly."

    return "\n\n---\n\n".join(selected)
