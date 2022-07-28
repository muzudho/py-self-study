"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv -c NonNumSVO1o0g1o4o0
"""
import argparse
import random
from src.dimport import Dimport

# Command line arguments
# ----------------------
ap = argparse.ArgumentParser()
ap.add_argument('-m', help='module')
ap.add_argument('-c', help='class')
args = ap.parse_args()

# Dynamic class import
# --------------------
NonNumSV = Dimport.load(args.m, args.c)

# Question
# --------
characters = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
# Shuffle
characters = ''.join(random.sample(characters, len(characters)))
print(f"question:{characters}")

# Answer
# ------
vec = NonNumSV.parse(characters)
print(f"answer:{vec}")

# Check
# -----
if vec is None:
    print("[Error] vec is none")
elif len(vec) < 2:
    print(f"[Error] vec length is small. len:{len(vec)} (< 2)")
else:
    is_error = False

    # もとの文字列と一致するかチェック
    text2 = ''.join(vec)
    if text2 != characters:
        is_error = True
        print("[Error] the string is different")
        print(f"> actual  :{text2}")
        print(f"> expected:{characters}")

    if not is_error:
        # 数字，非数字が 交互かチェック
        is_prev_numeric = vec[0].isnumeric()
        for i in range(1, len(vec)):
            is_numeric = vec[i].isnumeric()
            if is_prev_numeric == is_numeric:
                # Error
                is_error = True
                break

            is_prev_numeric = is_numeric

    if not is_error:
        print("correct!")
