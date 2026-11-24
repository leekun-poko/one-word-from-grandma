"""One Word From Grandma: write the single word to the entry file.

The entry is exactly one word: the word a grandma would text about AI.
She means ChatGPT. She types it the way she hears it, one letter bravely
misplaced, and sends it with total confidence.
"""

import os
from pathlib import Path

WORD = "chatgbt"


def output_path() -> Path:
    """Resolve the entry file location from the environment."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one word, no trailing newline: the word is the whole entry.
    path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
