"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
"""
import argparse
import random
from src.dimport import Dimport


def make_quiz():
    """答えのある問い作成"""
    quiz = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    # Shuffle
    quiz = ''.join(random.sample(quiz, len(quiz)))
    return quiz


def solve(quiz):
    """解く"""
    # Command line arguments
    # ----------------------
    ap = argparse.ArgumentParser()
    ap.add_argument('-m', help='module')
    ap.add_argument('-c', help='class')
    args = ap.parse_args()

    # Dynamic class import
    # --------------------
    NonNumSV = Dimport.load(args.m, args.c)

    return NonNumSV.to_answer(quiz)


def check(answer, quiz):
    """答え合わせ"""

    if answer is None:
        print("[Error] answer is none")
    elif len(answer) < 2:
        print(f"[Error] answer length is small. len:{len(answer)} (< 2)")
    else:
        is_error = False

        # もとの文字列と一致するかチェック
        text2 = ''.join(answer)
        if text2 != quiz:
            is_error = True
            print("[Error] the string is different")
            print(f"> actual  :{text2}")
            print(f"> expected:{quiz}")

        if not is_error:
            # 数字，非数字が 交互かチェック
            is_prev_numeric = answer[0].isnumeric()
            for i in range(1, len(answer)):
                is_numeric = answer[i].isnumeric()
                if is_prev_numeric == is_numeric:
                    # Error
                    is_error = True
                    break

                is_prev_numeric = is_numeric

        if not is_error:
            print("correct!")


# Plan
quiz = make_quiz()
print(f"quiz:{quiz}")

# Do
answer = solve(quiz)
print(f"answer:{answer}")

# Check
check(answer, quiz)
