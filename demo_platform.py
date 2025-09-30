#! /usr/bin/env python3
# Author: Diren Gunasekera
# Description: This script will demo HOWTO check which platform your
# program is running on..
"""
    Docstring:
"""

import sys
import os

print(sys.platform)

if sys.platform == "win32":
    print("Running on a windows platform")
elif sys.platform=="darwin":
    print("Running on MaxOSX platform")
elif sys.platform=="linux":
    print("Running on Linux platform")
else:
    print("On some other OS")

if sys.platform == "win32":
    my_home = os.environ["HOMEPATH"]
elif sys.platform=="darwin" or sys.platform=="linux":
    my_home = os.environ["HOME"]
else:
    print("On some other OS")

print("Home is", my_home)
