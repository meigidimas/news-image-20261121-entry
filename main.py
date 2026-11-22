#!/usr/bin/env python3
"""news-image-20261121 entry: copy the front-page image to the output dir.

Reads entry.png (JPEG bytes) shipped beside this file and writes the
identical bytes to $MAKEFUN_OUTPUT_DIR/entry.png (default /output),
creating the output directory first. Python 3.13, standard library only.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = SOURCE.read_bytes()
    TARGET.write_bytes(data)
    # Read back and confirm the copy is byte-identical to the source.
    assert TARGET.read_bytes() == data, "output differs from entry.png"


if __name__ == "__main__":
    main()
