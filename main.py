"""Duplicate the finished newspaper poster to the output folder.

This script takes the poster image that lives beside it and writes an
exact byte-for-byte duplicate to the destination directory. The output
directory is taken from the MAKEFUN_OUTPUT_DIR environment variable when
it is set, and defaults to /output otherwise. The destination folder is
created first if it is not already there, and the copy is checked by
comparing the size of the duplicate against the size of the original;
any mismatch raises an error instead of silently succeeding.

Only the Python standard library is used, and the script takes no
command-line arguments, opens no network connections, and introduces
no randomness, so running it twice over the same poster always
produces identical bytes.
"""

import os
import shutil
import sys

POSTER_NAME = "entry.png"

DEFAULT_OUTPUT_FOLDER = "/output"

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"


def locate_poster() -> str:
    """Return the path of the poster image next to this script."""
    script_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_folder, POSTER_NAME)


def choose_output_folder() -> str:
    """Pick the output folder from the environment, or the default."""
    chosen = os.environ.get(OUTPUT_DIR_ENV)
    if chosen:
        return chosen
    return DEFAULT_OUTPUT_FOLDER


def duplicate_poster(source_path: str, target_path: str) -> None:
    """Write an exact copy of the poster and check its size matches."""
    target_folder = os.path.dirname(target_path)
    if target_folder:
        os.makedirs(target_folder, exist_ok=True)
    shutil.copyfile(source_path, target_path)
    source_size = os.path.getsize(source_path)
    target_size = os.path.getsize(target_path)
    if source_size != target_size:
        raise ValueError(
            f"copy size mismatch: source {source_size} bytes, "
            f"copy {target_size} bytes"
        )


def run() -> int:
    """Copy the poster and report the result; nonzero on failure."""
    poster_path = locate_poster()
    output_folder = choose_output_folder()
    destination_path = os.path.join(output_folder, POSTER_NAME)
    duplicate_poster(poster_path, destination_path)
    print(f"copied {poster_path} -> {destination_path}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
