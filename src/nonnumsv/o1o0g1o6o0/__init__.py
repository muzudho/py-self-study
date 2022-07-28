"""
python -m tests.nonnumsv.o1o0g1o5o0.test -m src.nonnumsv.o1o0g1o6o0 -c NonNumSV
"""
import re


class NonNumSV:
    """Non-numeric separated value"""

    # * `^` - 文の始端
    # * `\d` - 半角数字
    # * `\d+` - 半角数字（1つ以上）
    # * `( )` - キャプチャーグループ
    __pat_num = re.compile(r"^(\d+)")
    # * `\D` - 半角数字以外
    __pat_nonnum = re.compile(r"^(\D+)")

    @staticmethod
    def to_answer(text):
        vec = []
        start = 0

        # 数字列か？
        m = NonNumSV.__pat_num.match(text[start:])
        if m:
            # 数字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

        while True:
            # 非数字の文字列か？
            m = NonNumSV.__pat_nonnum.match(text[start:])
            if m is None:
                break

            # 非数字の文字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

            # 数字列か？
            m = NonNumSV.__pat_num.match(text[start:])
            if m is None:
                break

            # 数字列だ
            token = m.group(1)
            vec.append(token)
            start += len(token)

        return vec
