"""Alien tourist's review of Earth, written out as a single line.

An alien visitor files a field note after two days on Earth: the
sunsets are stunning, the food is excellent, but the locals stare at
glowing rectangles all day. The note ends with a 4/5 rating, the way
a real review would.

The grader runs this script twice and compares the bytes, so the
output has to be exactly the same on every run.
"""

import hashlib
import os

REVIEW = (
    "Visited Earth. The sunsets are stunning, the food is excellent, "
    "but the dominant species spends all day staring at glowing "
    "rectangles. 4/5."
)


def check_entry(line):
    """Make sure the review fits the bounty gate; hand back UTF-8 bytes."""
    if not 1 <= len(line) <= 200:
        raise AssertionError("entry must be 1-200 characters")
    if not line.strip():
        raise AssertionError("entry must not be only white space")
    if "\n" in line or "\r" in line:
        raise AssertionError("entry must be a single line")
    return line.encode("utf-8")


def output_path():
    """Work out where entry.txt goes from the environment."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def report(path, data):
    """Print what was written so the run is easy to check."""
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


def confirm_written(path, data):
    """Read entry.txt back and confirm it holds exactly the review."""
    with open(path, "rb") as handle:
        stored = handle.read()
    assert stored == data, "entry.txt bytes differ from the review"
    assert stored.decode("utf-8") == REVIEW, "entry.txt text differs"
    assert stored == stored.rstrip(), "entry.txt has trailing whitespace"


def write_entry():
    """Encode the review, write it, confirm it, and report the result."""
    data = check_entry(REVIEW)
    path = output_path()
    with open(path, "wb") as handle:
        handle.write(data)
    confirm_written(path, data)
    report(path, data)


if __name__ == "__main__":
    write_entry()
