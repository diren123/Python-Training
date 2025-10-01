#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will demo
"""
    Docstring:
"""

def search_word(pattern, file):
    with(open(file, "rt") as fh_in):
        for (line_num, line) in enumerate(fh_in, start = 1):
            if line.isascii() and pattern in line:
                print(line_num, line, end = "")

    return None

search_word("done", r"words")
print("-" * 50)
search_word("banana", r"words")
print("-" * 50)