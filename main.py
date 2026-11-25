# SPDX-License-Identifier: MIT
"""Convince the AI Judge to Visit Your House: A Letter in One Image.

Copies the bundled invitation image (entry.png, next to this file) to
the grader's output directory, $MAKEFUN_OUTPUT_DIR/entry.png.
The repository is mounted read-only at grading time, so nothing is
ever written inside the repo itself.
"""

import os
import shutil


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Byte-identical copy: the bundled image is the entry, unchanged.
    assert os.path.getsize(src) == os.path.getsize(dst)
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
