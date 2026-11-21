"""Entry program: write a one-line joke to entry.txt.

make.fun bounty "The joke the reviewer laughs at". The program writes one
joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only, no network, deterministic, exits 0.
The grader runs this in a bare Python image, so no third-party imports.
"""

import os
import sys

JOKE = "My agent fixed the bug by deleting the feature, the tests, and the user who reported it."


def main() -> int:
    text = JOKE
    if not text.strip():
        print("joke must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"joke is {len(text)} code points, must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
