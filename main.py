import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# The joke: the agent is polite about its mistake, then makes the same mistake again.
JOKE = "My AI agent apologized for the bug, then reintroduced it in the fix."

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
