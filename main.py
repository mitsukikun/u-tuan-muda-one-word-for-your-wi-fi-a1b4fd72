#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

The entry is exactly one word describing home Wi-Fi as lived:
the signal is there, then it is not, then it is back again --
full bars in the hallway, gone the second you sit down to
watch something. The word is "peekaboo": the childhood game
of appearing and vanishing, instantly understood, funny at
once, and true to the most recognisable home Wi-Fi behaviour
(the vanishing act), not the tired slow/buffering/laggy
cliches. It also works as a Wi-Fi network name, which is
what the winning word becomes. The program writes the word
to /output/entry.txt (the harness path) and to entry.txt
next to this file.
"""

import os

# REVISED (v2): "yoyo" was true about the bars going up and down,
# but the laugh was weak -- it names fluctuation, not a joke.
# "peekaboo" is funnier and truer: Wi-Fi plays peekaboo --
# here, gone, here again -- and everyone has lived exactly that.
WORD = "peekaboo"


def main() -> None:
    word = WORD.strip()
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.strip() == word and " " not in word, "entry must be one word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(f"entry: {word!r} ({len(word)} chars)")


if __name__ == "__main__":
    main()
