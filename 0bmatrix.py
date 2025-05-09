import numpy as np
import os
import time
import random

RESET = "\033[0m"
GREEN = [
    "\033[92m",
    "\033[32m",
    "\033[38;5;40m",
    "\033[38;5;82m",
]
ALT = [
    "\033[38;5;196m",     # red
    "\033[38;5;226m",     # yellow
    # "\033[38;5;255m",     # white
]

def matrix():
    os.system('cls' if os.name == 'nt' else 'clear')

    size = os.get_terminal_size()
    rows = size.lines
    cols = size.columns

    padding = 2
    usable_rows = rows - padding * 2
    usable_cols = (cols // 2) - padding

    p_0 = np.random.uniform(0, 0.85)
    p_1 = 1 - p_0

    matrix = np.random.choice([0, 1], size=(usable_rows, usable_cols), p=[p_0,p_1])

    for _ in range(padding):
        print("" * usable_cols)

    for row in matrix:
        print(" " * (padding), end=" ")

        for val in row:
            if val == 0:
                color = random.choice(GREEN)
            else:
                color = random.choice(ALT)
            print(f"{color}{val}{RESET}", end=" ")

        print("" * (padding))

while True:
    matrix()
    time.sleep(0.1)