"""Six Words, One Story — make.fun bounty entry.

Writes exactly one six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python standard library, deterministic, no network.

The story: "Mars called. Earth let it ring."
Six words, one missed call from another world — a whole history of
contact, hope, and indifference in a single unanswered ring.
"""

import os

STORY = "Mars called. Earth let it ring."


def validate_story(story: str) -> None:
    """Guard the gate: exactly 6 words, single line, 1-60 code points."""
    if not story or story.strip() == "":
        raise ValueError("story must not be blank or only whitespace")
    if story != story.strip():
        raise ValueError("story must not start or end with whitespace")
    if "\n" in story or "\r" in story:
        raise ValueError("story must be a single line")
    if "  " in story or "\t" in story:
        raise ValueError("story must use single spaces between words")
    words = story.split(" ")
    if len(words) != 6:
        raise ValueError(f"story must be exactly 6 words, got {len(words)}")
    if not 1 <= len(story) <= 60:
        raise ValueError(
            f"story must be 1-60 Unicode code points, got {len(story)}"
        )


def main() -> None:
    validate_story(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    # Verify the round-trip: what landed on disk is exactly the story.
    with open(path, "r", encoding="utf-8") as f:
        validate_story(f.read().rstrip("\n"))


if __name__ == "__main__":
    main()
