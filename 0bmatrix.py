import numpy as np
import os
import time
import random

GREEN = "\033[91m"
RED = "\033[92m"
RESET = "\033[0m"

def matrix():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(np.random.randint(0, 2, size=(10, 10)))

while True:
    matrix()
    time.sleep(0.1)