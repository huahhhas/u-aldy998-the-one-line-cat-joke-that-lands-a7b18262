#!/usr/bin/env python3
"""Writes a single one-line cat joke to the output path.

Reads OUTPUT_PATH from the environment when set, otherwise writes to
/output/entry.txt. Pure standard library.
"""

import os
from pathlib import Path

JOKE = "My cat doesn't ignore me \u2014 he just schedules our quality time for 3 a.m., directly on my face."


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
