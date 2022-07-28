"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSVO1o0g1o6o0
"""
import re


class NonNumSVO1o0g1o6o0:
    """Non-numeric separated value"""

    # * `^ $` - 文の始端から終端まで
    # * `\d` - 半角数字
    # * `\D` - 半角数字以外
    # * `(?: )` - ただの括弧
    # * `( )?` - グループ，ただし省略可
    # * `( )*` - グループ，0個以上にマッチ
    __pat = re.compile(r"^(?:(\D+)?(\d+)?)*$")

    @staticmethod
    def parse(text):
        m = NonNumSVO1o0g1o6o0.__pat.match(text)

        if m:
            # タプルをリストに変換
            return list(m.groups())

        return None
