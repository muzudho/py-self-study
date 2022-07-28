"""
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o2o0 -c NonNumSV
"""
import argparse
from src.dimport import Dimport


def make_quiz():
    """答えのある問い作成"""
    return "ABC123DEF456GHI"


def solve(quiz):
    """解く"""

    # Command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-m', help='module')
    ap.add_argument('-c', help='class')
    args = ap.parse_args()

    # Dynamic class import
    NonNumSV = Dimport.load(args.m, args.c)

    return NonNumSV.parse(quiz)


def check(answer, quiz):
    """答え合わせ"""

    if answer is None:
        print("[Error] vec is none")
    else:
        vec_size = len(answer)
        if vec_size == 5:
            print("size is ok")
        else:
            print(f"[Error] the size is different. size:{vec_size}")

        if answer == ["ABC", "123", "DEF", "456", "GHI"]:
            print("correct!")
        else:
            print(f"[Error] the response is different. vec:{answer}")


# Plan
quiz = make_quiz()

# Do
answer = solve(quiz)

# Check
check(answer, quiz)
