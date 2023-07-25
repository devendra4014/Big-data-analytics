#!/usr/bin/python3

import sys
for line in sys.stdin:
    words = line.split()
    for word in words:
        word = word.lower()
        print(f"{word}\t{1}")
