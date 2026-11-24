#!/usr/bin/env python3
"""Write one satirical sentence to entry.txt.

The Long Roast: lawmakers who regulate AI, crypto and the internet
but cannot convert a file to PDF. Deterministic, no network, no clock.
"""

import os

ROAST = (
    "The lawmakers who just passed 412 pages of AI safety law still "
    "email their aides a file called FINAL_final_v7.docx and ask, "
    "IN ALL CAPS, how to turn it into a PDF."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
