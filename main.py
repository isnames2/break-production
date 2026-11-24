"""Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library; deterministic output, byte-identical on every run."""

import os

ENTRY = (
    "I deleted the production database. Every row, every table, gone. "
    "The backup job I wrote never ran once. I did this."
)
# ENTRY is 115 characters (limit 200), single line, no trailing spaces.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
