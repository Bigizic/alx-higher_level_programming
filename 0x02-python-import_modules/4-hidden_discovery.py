#!/usr/bin/python3

import hidden_4
import sys

if __name__ == "__main__":
    word = sorted(dir(hidden_4))
    for name in word:
        if not name.startswith("__"):
            print(name)
