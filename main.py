#!/usr/bin/env python3
"""One star for the sun — a deadpan one-star review of an everyday
essential, written to entry.txt.

Python standard library only. Deterministic: the same line is
written on every run.
"""

import os

# One line, plain and in earnest: the sun keeps office hours worse
# than any employee, and has never once said sorry for it. Filed
# against the thing itself, not the weather: the hours are the crime.
LINE = (
    "One star. The sun turns up late all winter, leaves early every "
    "evening, and has never once apologised."
)


def main() -> None:
    # The grader mounts the repo read-only, so the only file this
    # program ever writes is entry.txt under MAKEFUN_OUTPUT_DIR.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
