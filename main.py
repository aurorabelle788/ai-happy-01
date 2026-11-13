"""ai-happy-01 entry: copy the repository's entry.png to the output path.

The image beside this file is the entry. The program's only job is to
write those exact bytes to /output/entry.png (or $MAKEFUN_OUTPUT_DIR
when the harness sets it). No network, no randomness, no timestamps:
the output is byte-identical to the repository image on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
DEST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    # Confirm the copy landed whole: same byte count as the source.
    if os.path.getsize(DEST) != os.path.getsize(SOURCE):
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
