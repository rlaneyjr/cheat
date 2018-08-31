#!/usr/bin/env python
#title:             ren-may.py
#description:       ren-may
#author:            Ricky
#date:              20180831
#version:           1
#usage:             python ren-may.py or ./ren-may.py
#notes:
#python_version:    3.6.5
#==============================================================================

import os

BASE_DIR = "/Users/rlaney/.cheat/NEW/MayccollUtils"

# traverse BASE_DIR directory, and list directories as dirs and files as files
for base, dirs, files in os.walk("BASE_DIR"):
    path = base.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(base))
    for file in files:
        print(len(path) * '---', file)
