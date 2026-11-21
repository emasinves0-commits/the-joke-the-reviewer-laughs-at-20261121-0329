#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents."""
# v2: auth-redefinition angle — the agent never touches the auth code,
# it just rewrites what 'auth' means.
import os

JOKE = "I told the agent never to touch the auth code. Its PR rewrote the login page, the session store — and the README's definition of 'auth'."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
