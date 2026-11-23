"""Make the Judge Fall in Love in One Line.

Writes a single line of text to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

import os

LINE = "He kept her voicemail for six years \u2014 not for her voice, but for the pause before she said his name."

def main():
    # Gate self-check: the bounty requires /output/entry.txt to be UTF-8
    # text of 1 to 240 characters, not only whitespace, exactly one line.
    if not LINE or LINE.strip() == "":
        raise SystemExit("entry line is empty or only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be exactly one line")
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-240")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Atomic write: write to a temp file in the same directory, then rename
    # over entry.txt, so a partial write can never leave a broken entry.txt.
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.replace(tmp, target)

if __name__ == "__main__":
    main()
