#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
import os

# import subprocess


seeds_filename = "seeds.txt"

try:
    for line in open(seeds_filename, 'r+').readlines():
        # print(line)
        os.system("./main.py init -w=\"" + line.strip() + "\"")
        # lines = list(line for line in (l.strip() for l in f_in) if line)
        # if not line.strip():
        #     print(line)
        # subprocess.Popen( )
except:
    print("Seeds file not found")
