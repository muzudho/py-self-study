"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o7o0 --ac Answerer
"""
import re
import random

from ..o1o0g1o6o0 import Answerer as AnswererG1o6o0
#    ------------        --------    --------------
#    1                   2           3
# 1. 隣のフォルダー
# 2. クラス
# 3. 別名


class Answerer:
    """Non-numeric separated value"""

    # * `^` - 文の始端
    # * `\d` - 半角数字
    # * `\d+` - 半角数字（1つ以上）
    # * `( )` - キャプチャーグループ
    __pat_num = re.compile(r"^(\d+)")
    # * `\D` - 半角数字以外
    __pat_nonnum = re.compile(r"^(\D+)")

    @staticmethod
    def to_answer(quiz):
        answer = AnswererG1o6o0.to_answer(quiz)

        # 要素数
        length = len(answer)

        # 要素が２個に満たなければスワップできません
        if length <= 2:
            raise ValueError(f"Couldn't swap. length:{length}")

        # ランダムなインデックスを２つ取得
        i1 = random.randint(1, length-1)
        i2 = random.randint(0, i1-1)

        # スワップ
        temp = answer[i1]
        answer[i1] = answer[i2]
        answer[i2] = temp

        return answer
