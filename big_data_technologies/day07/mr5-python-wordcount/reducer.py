#!/usr/bin/python3

import sys

word_dict = dict()
for line in sys.stdin:
    (word,cnt) = line.split()
    oldcnt = word_dict.get(word, 0)
    word_dict[word] = oldcnt + int(cnt)

for word,total in word_dict.items():
    print(f"{word}\t{total}")
