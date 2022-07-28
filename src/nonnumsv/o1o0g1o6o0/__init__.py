"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o6o0 --ac Answerer
"""
import re


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
        answer = []
        start = 0

        # 数字列か？
        m = Answerer.__pat_num.match(quiz[start:])
        if m:
            # 数字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

        while True:
            # 非数字の文字列か？
            m = Answerer.__pat_nonnum.match(quiz[start:])
            if m is None:
                break

            # 非数字の文字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

            # 数字列か？
            m = Answerer.__pat_num.match(quiz[start:])
            if m is None:
                break

            # 数字列だ
            token = m.group(1)
            answer.append(token)
            start += len(token)

        return answer
