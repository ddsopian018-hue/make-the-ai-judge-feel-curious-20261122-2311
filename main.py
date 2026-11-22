"""Make the AI judge feel curious — a lighthouse that should be dark.

Writes a single short text to ``<output dir>/entry.txt``. The output
directory comes from the MAKEFUN_OUTPUT_DIR environment variable when
the grader sets it, and falls back to ``/output`` otherwise.

The text is one scene with a small impossibility at its centre: a
lighthouse dead for thirty years, cut off from every source of
power, that blinked twice at three in the morning. The facts are
stated plainly and in order — the cable cut in 1994, no keeper, no
bulb, no power, an empty harbour log — and the last sentence leaves
the reader with the gulls going quiet first, an image that keeps
working after the text ends. Nothing in it tells the reader what to
feel; the curiosity comes from the detail that does not add up.
"""

import os

TEXT = (
    "The lighthouse on the point has been dark for thirty years. "
    "The town cut its cable in 1994; there is no keeper, no bulb, "
    "no power. Last night, at three in the morning, it blinked "
    "twice. The harbour log shows nothing. The gulls went quiet "
    "first."
)


def _check(text: str) -> int:
    """Return the code-point count, or fail if the text is invalid.

    The gate requires 1-280 Unicode code points and text that is
    not whitespace only. ``len()`` on a Python string counts code
    points, which is exactly the unit the gate measures.
    """
    size = len(text)
    if size < 1 or size > 280:
        raise SystemExit(f"entry text is {size} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("entry text must not be whitespace only")
    return size


def main() -> None:
    size = _check(TEXT)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(TEXT)

    print(f"wrote {size} code points to {target}")


if __name__ == "__main__":
    main()
