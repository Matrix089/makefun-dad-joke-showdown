"""Dad Joke Showdown entry (round 2).

Writes one original dad joke to /output/entry.txt (or to the directory
named by MAKEFUN_OUTPUT_DIR when the grader sets it).

The joke is written to be told out loud: a household setup, a clean pun
that lands on the first read, and the punchline at the end.
"""

import os

JOKE = "I told the elevator it had a great sense of humor. It said thanks — it's just trying to lift everyone's spirits."


def main():
    joke = JOKE.strip()
    if not 1 <= len(joke) <= 200:
        raise SystemExit(f"Joke must be 1 to 200 characters, got {len(joke)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)
    # Read it back to confirm what was written is exactly the joke.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != joke:
        raise SystemExit("Read-back mismatch: entry.txt does not match the joke")
    print(f"Wrote {len(joke)} characters to {path}")


if __name__ == "__main__":
    main()
