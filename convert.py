#!/usr/bin/env python
#title:             convert.py
#description:       Convert File Names
#author:            Ricky Laney
#date:              20180801
#version:           0.1
#usage:             python convert.py or ./convert.py
#notes:
#python_version:    3.6.5
#==============================================================================

import os
import sys

# Convert man to html
zcat /usr/share/man/man1/man.1.gz  | groff -mandoc -Thtml
