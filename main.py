"""Ship the finished front page for Tuesday 24 November 2026.

The poster is stored next to this file as entry.png: a black-and-white
newspaper front page that sums up the day's world news under the masthead
"THE WORLD TODAY". This program does one thing only — it copies that file,
byte for byte, to /output/entry.png (or to $MAKEFUN_OUTPUT_DIR when that is
set), creating the destination folder first.

It uses nothing but the Python standard library, takes no arguments, reads
no network and makes no random choices, so running it twice writes the
same bytes twice.
"""

import os
from pathlib import Path

POSTER = Path(__file__).resolve().parent / "entry.png"


def output_path() -> Path:
    """Return where the poster must land."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.png"


def main() -> None:
    poster_bytes = POSTER.read_bytes()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(poster_bytes)
    if target.read_bytes() != poster_bytes:
        raise RuntimeError("copy mismatch: %s differs from %s" % (target, POSTER))


if __name__ == "__main__":
    main()
