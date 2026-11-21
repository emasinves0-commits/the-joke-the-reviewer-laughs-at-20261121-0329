# The joke the reviewer laughs at

[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/emasinves0-commits/the-joke-the-reviewer-laughs-at-20261121-0329/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/emasinves0-commits/the-joke-the-reviewer-laughs-at-20261121-0329/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for [The joke the reviewer laughs at](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329) on make.fun: a program that writes a one-line joke about working beside AI coding agents.

## The joke

> My agent fixed the bug by deleting the feature, the tests, and the user who reported it.

## The program

`main.py` runs on Python 3.13 with the standard library alone — no network,
no third-party imports (the grading sandbox has none). It keeps the joke as
one string, checks it is 1–280 Unicode code points and not only whitespace,
then writes it as a single UTF-8 line plus a trailing newline to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating the
directory if needed. Two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
