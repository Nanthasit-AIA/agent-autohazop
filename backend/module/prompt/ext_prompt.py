from pathlib import Path

_PROMPT_DIR = Path(__file__).parent

def _load_skill() -> tuple[str, str]:
    system = (_PROMPT_DIR / "skill.md").read_text(encoding="utf-8")
    user_template = (_PROMPT_DIR / "skill_user.md").read_text(encoding="utf-8")
    return system, user_template

PID_SYSTEM_PROMPT, _PID_USER_TEMPLATE = _load_skill()


def build_pid_input(
    process_description: str,
    file_ids: list[str],
    *,
    node_define: str = "",
    intention: str = "",
) -> list[dict]:
    node_define_text = node_define.strip() or "(not provided — auto-define nodes based on the P&ID layout)"
    intention_text = intention.strip() or "(not provided — derive from P&ID and process description)"

    user_text = _PID_USER_TEMPLATE.format(
        node_define=node_define_text,
        intention=intention_text,
        process_description=process_description,
    )

    content: list[dict] = [{"type": "input_text", "text": user_text}]
    content.extend({"type": "input_file", "file_id": fid} for fid in file_ids)

    return [{"role": "user", "content": content}]
