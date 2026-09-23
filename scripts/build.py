#!/usr/bin/env python3
"""Combine each bot's instructions with the shared knowledge files into one
paste-ready file per bot in ready-to-paste/. Re-run after editing any file in
agents/ or knowledge/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = [
    "company-profile.md",
    "brand-voice.md",
    "ideal-customers.md",
    "sales-playbook.md",
    "rules-and-compliance.md",
]
MARKER = "## Instructions (paste into Grok Bot)"


def main() -> None:
    out_dir = ROOT / "ready-to-paste"
    out_dir.mkdir(exist_ok=True)
    knowledge = "\n\n---\n\n".join(
        (ROOT / "knowledge" / name).read_text().strip() for name in KNOWLEDGE
    )
    sheet = (ROOT / "templates" / "google-sheet-setup.md").read_text().strip()

    for agent in sorted((ROOT / "agents").glob("*.md")):
        text = agent.read_text()
        header, _, instructions = text.partition(MARKER)
        if not instructions:
            raise SystemExit(f"{agent.name}: missing '{MARKER}' section")
        title = header.splitlines()[0].lstrip("# ").strip()
        combined = (
            f"# {title}\n\n"
            f"{instructions.strip()}\n\n"
            "---\n\n# REFERENCE KNOWLEDGE (follow these at all times)\n\n"
            f"{knowledge}\n\n---\n\n{sheet}\n"
        )
        (out_dir / agent.name).write_text(combined)
        print(f"wrote ready-to-paste/{agent.name} ({len(combined):,} chars)")


if __name__ == "__main__":
    main()
