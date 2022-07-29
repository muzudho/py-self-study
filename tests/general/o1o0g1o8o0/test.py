"""
Example
-------
python -m tests.general.o1o0g1o8o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --oam src.nonnumsv.o1o0g1o6o0 --oac Answerer --xam src.nonnumsv.o1o0g1o7o0 --xac Answerer --o 1000 --x 1000
"""
import argparse
import random
import math
from src.dimport import Dimport  # Dynamic class import

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('--qm', help='questioner module')
ap.add_argument('--qc', help='questioner class')
ap.add_argument('--oam', help='correct answerer module')
ap.add_argument('--oac', help='correct answerer class')
ap.add_argument('--xam', help='incorrect answerer module')
ap.add_argument('--xac', help='incorrect answerer class')
ap.add_argument('--o', help='correct total count')
ap.add_argument('--x', help='incorrect total count')
args = ap.parse_args()

# Plan
# ----
Questioner = Dimport.load(args.qm, args.qc)
quest = Questioner()

CorrectAnswerer = Dimport.load(args.oam, args.oac)
IncorrectAnswerer = Dimport.load(args.xam, args.xac)
correct_total = int(args.o)
incorrect_total = int(args.x)


def check_correct(total):
    """正答数を数える"""
    correct_count = 0
    for i in range(0, total):
        quiz = quest.make_quiz()
        answer = CorrectAnswerer.to_answer(quiz)
        err = quest.check(answer, quiz)
        if err is None:
            correct_count += 1

    return correct_count


def check_incorrect(total):
    """誤答数を数える"""
    incorrect_count = 0
    for i in range(0, total):
        quiz = quest.make_quiz()
        answer = IncorrectAnswerer.to_answer(quiz)
        err = quest.check(answer, quiz)
        if not err is None:
            incorrect_count += 1

    return incorrect_count


# Do
# --
correct_rest = correct_total
incorrect_rest = incorrect_total
correct_count = 0
incorrect_count = 0

# Example
if 0 < correct_rest:
    quiz = quest.make_quiz()
    print(f"(1) quiz:{quiz}")
    answer = CorrectAnswerer.to_answer(quiz)
    print(f"    answer:{answer}")
    err = quest.check(answer, quiz)
    if err is None:
        correct_count += 1
    else:
        print(err)
    correct_rest -= 1

# Example
if 0 < incorrect_rest:
    quiz = quest.make_quiz()
    print(f"(2) quiz:{quiz}")
    answer = IncorrectAnswerer.to_answer(quiz)
    print(f"    answer:{answer}")
    err = quest.check(answer, quiz)
    if not err is None:
        print(err)
        incorrect_count += 1
    incorrect_rest -= 1

print("...")

while 0 < correct_rest or 0 < incorrect_rest:
    # 正答テスト
    if 0 < correct_rest:
        if incorrect_rest == 0:
            times = correct_rest
        else:
            # 正答テストの残り件数の方が多かったら多めに行う
            scale = math.ceil(correct_rest / incorrect_rest)
            # ランダムに少し上乗せしてリズムを狂わす
            scale += random.randint(0, 3)
            times = min(scale, correct_rest)
        correct_count += check_correct(times)
        correct_rest -= times

    # 誤答テスト
    if 0 < incorrect_rest:
        if correct_rest == 0:
            times = incorrect_rest
        else:
            # 誤答テストの残り件数の方が多かったら多めに行う
            scale = math.ceil(incorrect_rest / correct_rest)
            # ランダムに少し上乗せしてリズムを狂わす
            scale += random.randint(0, 3)
            times = min(scale, incorrect_rest)
        incorrect_count += check_incorrect(times)
        incorrect_rest -= times

total_count = correct_total + incorrect_total
quality = (correct_count + incorrect_count) * 100 / total_count


# Check
# -----
print(f"""quality:{quality:.1f}% total:{total_count}""")
