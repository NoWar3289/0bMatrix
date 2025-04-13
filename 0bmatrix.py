import numpy as np
import os
import time
import random

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
PADDING_COLOR = "\033[31m"

def matrix():
    os.system('cls' if os.name == 'nt' else 'clear')

    size = os.get_terminal_size()
    row = size.lines
    col = size.columns

    padding = 1
    usable_rows = row - padding * 2
    usable_cols = (col // 2) - padding * 2

    p_0 = np.random.uniform(0,0.75)
    p_1 = 1 - p_0

    matrix = np.random.choice([0, 1], size=(usable_rows, usable_cols), p=[p_0,p_1])

    for _ in range(padding):
        print(f"{PADDING_COLOR}{' ' * col}{RESET}")

    for row in matrix:
        
        print(PADDING_COLOR + "  " * (padding), end="")

        for val in row:
            if val == 0:
                print(f"{RED}{val}{RESET}", end="")
            else:
                print(f"{GREEN}{val}{RESET}", end="")

        print(PADDING_COLOR + " " * (padding) + RESET)

while True:
    matrix()
    time.sleep(0.1)