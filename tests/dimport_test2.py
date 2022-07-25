"""
python -m tests.dimport_test2 -m src.hello -c Hello
"""
import argparse
from src.dimport import Dimport

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

print(Dimport.load(args.m, args.c).message)
