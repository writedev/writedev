from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from typing import Tuple

README_PATH = Path(__file__).with_name("README.md")


def _compile_block_pattern(tag: str) -> re.Pattern[str]:
    """Return a compiled regex that matches both visible and hidden block states."""
    tag_pattern = re.escape(tag)
    return re.compile(
        rf"(?P<indent>[ \t]*)<!--{tag_pattern}(?P<visible>-->)?(?P<newline>\r?\n)"
        rf"(?P<body>.*?)(?P<closing_newline>\r?\n)(?P=indent)"
        rf"(?P<closing><!--{tag_pattern}_END-->|{tag_pattern}_END-->)",
        re.DOTALL,
    )


def toggle_block(text: str, tag: str, enable: bool) -> Tuple[str, bool]:
    """Toggle visibility of a README section surrounded by special HTML comments."""
    pattern = _compile_block_pattern(tag)

    def replacement(match: re.Match[str]) -> str:
        indent = match.group("indent") or ""
        first_newline = match.group("newline") or "\n"
        second_newline = match.group("closing_newline") or "\n"
        body = match.group("body")

        if enable:
            return (
                f"{indent}<!--{tag}-->{first_newline}"
                f"{body}"
                f"{second_newline}{indent}<!--{tag}_END-->"
            )

        return (
            f"{indent}<!--{tag}{first_newline}"
            f"{body}"
            f"{second_newline}{indent}{tag}_END-->"
        )

    updated_text, count = pattern.subn(replacement, text)
    if count == 0:
        print(f"[update_readme] Block '{tag}' introuvable.", file=sys.stderr)
        return text, False

    return updated_text, True


def main() -> None:
    content = README_PATH.read_text(encoding="utf-8")
    # hour = dt.datetime.utcnow().hour
    hour = 1
    show_hour_one = hour % 2 == 0

    updated, changed_first = toggle_block(content, "HOUR_1", show_hour_one)
    updated, changed_second = toggle_block(updated, "HOUR_2", not show_hour_one)

    if changed_first or changed_second:
        README_PATH.write_text(updated, encoding="utf-8")
    else:
        print(
            "[update_readme] Aucun bloc cible n'a été mis à jour; fichier inchangé.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
