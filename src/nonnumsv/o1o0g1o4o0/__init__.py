"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
"""
import re


class Answerer:
    """Non-numeric separated value"""

    # * `^` - 行頭
    # * `( )` - キャプチャーグループ
    # * `[A-Z]` - 大文字のAからZ
    # * `[ ]+` - 1回以上
    # * `[0-9]` - 半角数字の0から9
    # * `$` - 行末
    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def to_answer(quiz):
        m = Answerer.__pat.match(quiz)
        if m:
            # `m.group( )` - 引数の数はパターンの括弧の位置に対応
            return [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]

        return None
