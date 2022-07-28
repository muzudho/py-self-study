"""
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv -c NonNumSV
"""
import argparse
from src.dimport import Dimport

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

# Dynamic class import
NonNumSV = Dimport.load(args.m, args.c)

# Code
vec = NonNumSV.parse("ABC123DEF456GHI")

if vec is None:
    print("[Error] vec is none")
else:
    vec_size = len(vec)
    if vec_size == 5:
        print("size is ok")
    else:
        print(f"[Error] the size is different. size:{vec_size}")

    if vec == ["ABC", "123", "DEF", "456", "GHI"]:
        print("correct!")
    else:
        print(f"[Error] the response is different. vec:{vec}")
