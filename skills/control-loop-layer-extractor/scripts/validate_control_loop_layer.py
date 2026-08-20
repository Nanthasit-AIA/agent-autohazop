#!/usr/bin/env python3
"""Validate ControlLoopLayer JSON using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "schema_version",
    "function_name",
    "status",
    "inputs_used",
    "control_loops",
    "nodes",
    "edges",
    "missing_evidence",
    "validation",
}

REQUIRED_LOOP_FIELDS = {
    "loop_id",
    "classification",
    "measured_variable",
    "controller",
    "final_elements",
    "controlled_assets",
    "edges",
    "provenance",
    "confidence",
    "missing_basis",
    "hazop_relevance",
}

REQUIRED_COMPONENT_FIELDS = {"id", "tag", "role", "attachment", "confidence"}
REQUIRED_PROVENANCE_FIELDS = {"source_file", "method", "confidence", "activity"}
VALID_CONFIDENCE_MIN = 0.0
VALID_CONFIDENCE_MAX = 1.0


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def check_confidence(value: Any, path: str, issues: list[str]) -> None:
    if not is_number(value):
        issues.append(f"{path}: confidence must be numeric")
        return
    if value < VALID_CONFIDENCE_MIN or value > VALID_CONFIDENCE_MAX:
        issues.append(f"{path}: confidence must be between 0 and 1")


def require_keys(obj: dict[str, Any], keys: set[str], path: str, issues: list[str]) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        issues.append(f"{path}: missing required keys: {', '.join(missing)}")


def validate_provenance(items: Any, path: str, issues: list[str]) -> None:
    if not isinstance(items, list) or not items:
        issues.append(f"{path}: provenance must be a non-empty list")
        return
    for idx, item in enumerate(items):
        item_path = f"{path}[{idx}]"
        if not isinstance(item, dict):
            issues.append(f"{item_path}: provenance item must be an object")
            continue
        require_keys(item, REQUIRED_PROVENANCE_FIELDS, item_path, issues)
        if "confidence" in item:
            check_confidence(item["confidence"], f"{item_path}.confidence", issues)
        methods = item.get("method")
        if not isinstance(methods, list) or not all(isinstance(method, str) for method in methods):
            issues.append(f"{item_path}.method: must be a list of strings")


def validate_component(component: Any, path: str, issues: list[str]) -> None:
    if not isinstance(component, dict):
        issues.append(f"{path}: component must be an object")
        return
    require_keys(component, REQUIRED_COMPONENT_FIELDS, path, issues)
    if "confidence" in component:
        check_confidence(component["confidence"], f"{path}.confidence", issues)
    attachment = str(component.get("attachment", "")).strip().lower()
    if not attachment:
        issues.append(f"{path}.attachment: must be explicit or 'unknown'")


def validate_loop(loop: Any, index: int, edge_ids: set[str], issues: list[str]) -> None:
    path = f"control_loops[{index}]"
    if not isinstance(loop, dict):
        issues.append(f"{path}: loop must be an object")
        return
    require_keys(loop, REQUIRED_LOOP_FIELDS, path, issues)
    if "confidence" in loop:
        check_confidence(loop["confidence"], f"{path}.confidence", issues)
    validate_component(loop.get("controller"), f"{path}.controller", issues)
    for field in ("final_elements", "controlled_assets"):
        value = loop.get(field)
        if not isinstance(value, list) or not value:
            issues.append(f"{path}.{field}: must be a non-empty list")
            continue
        for idx, component in enumerate(value):
            validate_component(component, f"{path}.{field}[{idx}]", issues)
    for idx, component in enumerate(loop.get("sensors", []) if isinstance(loop.get("sensors", []), list) else []):
        validate_component(component, f"{path}.sensors[{idx}]", issues)
    validate_provenance(loop.get("provenance"), f"{path}.provenance", issues)
    loop_edges = loop.get("edges")
    if not isinstance(loop_edges, list):
        issues.append(f"{path}.edges: must be a list")
    else:
        for edge_id in loop_edges:
            if edge_id not in edge_ids:
                issues.append(f"{path}.edges: edge id not found in top-level edges: {edge_id}")
    hazop = loop.get("hazop_relevance")
    if not isinstance(hazop, dict):
        issues.append(f"{path}.hazop_relevance: must be an object")
    else:
        for key in ("usable_for_hazop", "cause_families", "safeguard_claims", "recommendation_hooks"):
            if key not in hazop:
                issues.append(f"{path}.hazop_relevance: missing {key}")


def validate_node(node: Any, index: int, issues: list[str]) -> str | None:
    path = f"nodes[{index}]"
    if not isinstance(node, dict):
        issues.append(f"{path}: node must be an object")
        return None
    require_keys(node, {"id", "type", "label", "layer", "attributes", "provenance"}, path, issues)
    validate_provenance(node.get("provenance"), f"{path}.provenance", issues)
    return node.get("id") if isinstance(node.get("id"), str) else None


def validate_edge(edge: Any, index: int, node_ids: set[str], issues: list[str]) -> str | None:
    path = f"edges[{index}]"
    if not isinstance(edge, dict):
        issues.append(f"{path}: edge must be an object")
        return None
    require_keys(edge, {"id", "source", "target", "type", "layer", "attributes", "provenance"}, path, issues)
    edge_id = edge.get("id") if isinstance(edge.get("id"), str) else None
    for endpoint in ("source", "target"):
        value = edge.get(endpoint)
        if isinstance(value, str) and value not in node_ids and not value.startswith("external:"):
            issues.append(f"{path}.{endpoint}: endpoint does not match a node id or external boundary: {value}")
    validate_provenance(edge.get("provenance"), f"{path}.provenance", issues)
    return edge_id


def validate(data: dict[str, Any]) -> dict[str, Any]:
    issues: list[str] = []
    require_keys(data, REQUIRED_TOP_LEVEL, "$", issues)
    if data.get("schema_version") != "control-loop-layer-0.1":
        issues.append("$.schema_version: must be control-loop-layer-0.1")
    if data.get("function_name") != "extract_control_loop_layer":
        issues.append("$.function_name: must be extract_control_loop_layer")

    nodes = data.get("nodes")
    edges = data.get("edges")
    loops = data.get("control_loops")
    if not isinstance(nodes, list):
        issues.append("$.nodes: must be a list")
        nodes = []
    if not isinstance(edges, list):
        issues.append("$.edges: must be a list")
        edges = []
    if not isinstance(loops, list):
        issues.append("$.control_loops: must be a list")
        loops = []

    node_ids: set[str] = set()
    for idx, node in enumerate(nodes):
        node_id = validate_node(node, idx, issues)
        if node_id:
            if node_id in node_ids:
                issues.append(f"nodes[{idx}].id: duplicate node id {node_id}")
            node_ids.add(node_id)

    edge_ids: set[str] = set()
    for idx, edge in enumerate(edges):
        edge_id = validate_edge(edge, idx, node_ids, issues)
        if edge_id:
            if edge_id in edge_ids:
                issues.append(f"edges[{idx}].id: duplicate edge id {edge_id}")
            edge_ids.add(edge_id)

    for idx, loop in enumerate(loops):
        validate_loop(loop, idx, edge_ids, issues)

    return {
        "passed": not issues,
        "issue_count": len(issues),
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ControlLoopLayer JSON")
    parser.add_argument("json_path", type=Path)
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args()

    try:
        data = json.loads(args.json_path.read_text(encoding="utf-8"))
    except Exception as exc:
        result = {"passed": False, "issue_count": 1, "issues": [f"Failed to read JSON: {exc}"]}
    else:
        if not isinstance(data, dict):
            result = {"passed": False, "issue_count": 1, "issues": ["Top-level JSON must be an object"]}
        else:
            result = validate(data)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Passed: {result['passed']}")
        print(f"Issues: {result['issue_count']}")
        for issue in result["issues"]:
            print(f"- {issue}")

    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

