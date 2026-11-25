"""The 3AM Fridge Text: write the one line a smart fridge texts its owner.

The program writes a single line to /output/entry.txt. The line is the
whole entry: it must read like a text message a smart fridge would send
its owner at 3am, funny on its own, in the fridge's small voice.
"""

import os

LINE = (
    "3am. I kept everything cold all night, and you repay me by standing "
    "here in the dark, eating pickles over the sink like a raccoon."
)


def main() -> None:
    # The gate only accepts 1-140 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 140:
        raise ValueError(
            f"entry line must be one line of 1-140 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
