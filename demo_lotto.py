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
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate Number = ", num)

print("Lottery numbers = ", lotto)
