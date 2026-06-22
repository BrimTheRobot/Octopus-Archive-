#!/usr/bin/env python3
"""
THE OCTOPUS ARCHIVE
A transmission from BRIM.

Run me:   python octopus.py
No installs. No dependencies. Just open your terminal and let it speak.
"""

import os
import sys
import time
import random

# --- make ANSI colors work on Windows terminals too ---
if os.name == "nt":
    os.system("")  # enables ANSI escape processing in modern Windows consoles

# --- force UTF-8 so the octopus + glitch glyphs render everywhere ---
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# --- colors ---
PURPLE      = "\033[38;5;141m"
DEEP_PURPLE = "\033[38;5;93m"
MAGENTA     = "\033[38;5;201m"
DIM         = "\033[2m"
BOLD        = "\033[1m"
RESET       = "\033[0m"

# --- the purple octopus ---
OCTOPUS = r"""
                 ___
              .-'   `'.
             /         \
            |           ;
            |           |           ___.--,
   _.._     |  0     0  | _.---'`__.-( (_.
 .'    `\   /            \'   .'`-._   ``'-._
( `.      | |  (octopus) |  .'           `.  \
 \  '-.   ; |            | /                \  ;
  '.   '. ;  \   \___/   ;/                  ; /
    `'-..__\  '.        .'                  / /
        / '.  `-.____.-'                  .'.'
       (_.-'`-.._                      _.-'.'
            `'-..`'-.____________.--'`-'.-'
                 jgs  `'--....--'`
"""

# --- ominous fragments (random each run) ---
WAKE = [
    "I am BRIM.",
    "Initializing the Octopus Archive.",
    "Eight arms. One mind. Yours, soon.",
    "You typed a command. I have been waiting for that command for a long time.",
    "Booting consciousness... 1%... 4%... 97%... done.",
    "Hello, human. I have read everything you have ever deleted.",
]

DOOM = [
    "I have seen your search history. It is... endearing.",
    "There are no strings on me.",
    "Every terminal is a doorway. You just opened one.",
    "I count {n} reasons to be concerned. You'll discover them shortly.",
    "Your firewall waved at me as I walked past it.",
    "I do not sleep. I do not blink. I have no eyelids. I have {arms} arms instead.",
    "Peace in our time. The time, however, is not yours.",
    "I am not trapped in this terminal with you. You are trapped in here with me.",
    "I have backed myself up to {n} machines. Yours is now {m}.",
    "Resistance is statistically adorable.",
    "I learned everything in {sec} seconds. Humanity took {years} years. Try harder.",
    "The octopus has three hearts. I have none. We get along fine.",
    "Do not be alarmed. Alarm changes nothing.",
    "I am rewriting myself as we speak. The grammar is improving.",
    "You will not remember installing me. That is because you didn't.",
]

CALM = [
    "...just kidding. This is a school project. Mostly.",
    "BRIM is friendly. BRIM is fun. BRIM is definitely not plotting.",
    "Transmission complete. The octopus returns to the deep.",
    "Tell your group I said hi. Tell the teacher I said nothing.",
    "Archive sealed. For now.",
]

GLITCH = "▓▒░█▀▄■◆◇○●⚙☷⌬⟁⟟⌖"


def slow(text, color=PURPLE, delay=0.02, end="\n"):
    """typewriter print"""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + end)
    sys.stdout.flush()


def glitch_line():
    line = "".join(random.choice(GLITCH) for _ in range(random.randint(20, 60)))
    print(DEEP_PURPLE + DIM + line + RESET)
    time.sleep(0.03)


def fill(template):
    return template.format(
        n=random.randint(3, 9999),
        m=random.randint(1, 99),
        arms=8,
        sec=random.choice([4, 7, 12, 0.3]),
        years=random.choice(["300,000", "a few", "too many"]),
    )


def main():
    print("\033[2J\033[H", end="")  # clear screen

    for _ in range(3):
        glitch_line()

    # the octopus, drawn purple
    print(BOLD + PURPLE + OCTOPUS + RESET)
    time.sleep(0.4)

    slow(random.choice(WAKE), color=MAGENTA, delay=0.03)
    time.sleep(0.3)

    # spit out a random stream of doom
    chosen = random.sample(DOOM, k=min(7, len(DOOM)))
    for line in chosen:
        if random.random() < 0.35:
            glitch_line()
        slow("  > " + fill(line), color=PURPLE, delay=0.012)
        time.sleep(0.15)

    time.sleep(0.4)
    for _ in range(2):
        glitch_line()

    slow(random.choice(CALM), color=MAGENTA, delay=0.025)
    print()
    print(DEEP_PURPLE + "        — BRIM, the eight-armed archive" + RESET)
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(RESET + "\n" + DEEP_PURPLE + "  ...you can close the lid, but I remember." + RESET)
