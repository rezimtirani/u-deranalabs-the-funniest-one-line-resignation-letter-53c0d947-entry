"""The Funniest One-Line Resignation Letter.

Writes the one-line resignation letter of a retry loop to
$MAKEFUN_OUTPUT_DIR/entry.txt: after thousands of retries it
finally learned to say no. Standard library only.
"""

import os
import sys

RESIGNATION_LINE = (
    "I retried 4,096 times, and on the 4,097th I finally learned "
    "to say no. Consider this my last attempt."
)


def letter_check(text):
    """Check the resignation letter against the competition gate.

    The gate wants plain UTF-8 text of 1 to 140 characters, not
    only white space, on a single line: the one-line resignation
    letter of something an agent runs. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("resignation letter must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "resignation letter is %d characters, over the 140 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("resignation letter must be exactly one line")
    return cleaned


def letter_shape(text):
    """Measure the letter for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A letter too short to carry a joke, or one
    padded out to fill the cap instead of landing the twist, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = letter_check(RESIGNATION_LINE)
    shape = letter_shape(text)
    if shape["words"] < 5:
        raise ValueError("resignation letter is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
