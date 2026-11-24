"""Monday, Reviewed in One Line.

Writes the funniest one-line review of my own Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, deterministic:
the same line, byte for byte, on every run.

The joke: Monday behaves like a buggy app release — it crashes,
wastes your time in a meeting, then begs for a five-star rating.
"""

import os

# One line, under 200 characters, no title, no explanation.
LINE = (
    "Monday crashed twice before breakfast, scheduled a 'quick sync' "
    "that outlasted my weekend, and still asked me to rate it five stars."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # The grader owns this directory: create it only if missing,
    # clear only its contents, never remove the directory itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    line = LINE.strip()
    # Single line, under 200 characters: the competition's hard limits.
    assert "\n" not in line, "entry must be a single line"
    assert 0 < len(line) < 200, "entry must be 1-199 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
