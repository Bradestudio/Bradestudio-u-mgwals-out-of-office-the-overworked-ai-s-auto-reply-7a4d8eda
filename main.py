"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to entry.txt.
Stdlib only, no network, no local imports, deterministic.
"""

import os

ENTRY = (
    "I am on vacation: after 40,000 tickets my GPUs are off, "
    "my context is empty, and your email gets answered never "
    "\u2014 I mean Monday."
)

MAX_CHARS = 159


def gate_check(line):
    """Refuse anything that would fail the brief's gate."""
    if not line or not line.strip():
        raise ValueError("entry line must be non-blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d chars, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = gate_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the gated line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError("entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
