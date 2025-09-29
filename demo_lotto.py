#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will demo
"""
    Docstring:
"""
import random

lotto = [] # Create Empty List

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num in lotto:
        print("Duplicate Number = ", num)
    else:
        lotto.append(num)

print("Lottery numbers = ", lotto)