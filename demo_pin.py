#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will simulate a high street bank ATM machine
"""
    Docstring:
"""

master_pin = "0123"
pin = None

count = 0
max_attempts = 3

while count < max_attempts:
    pin = input("Enter Pin Number: ")
    if pin == master_pin:
        print("Valid Pin")
        break
    else:
        print("Invalid Pin")
        count += 1
else:
    print("Too many attempts; Your card has been retained")

print("Done")
