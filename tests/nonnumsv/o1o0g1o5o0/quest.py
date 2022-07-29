"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac Answerer
"""
import random


class Questioner:
    """出題者"""

    def make_quiz(self):
        """答えのある問い作成"""
        quiz = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        # Shuffle
        quiz = ''.join(random.sample(quiz, len(quiz)))
        return quiz

    def check(self, answer, quiz):
        """答え合わせ
        Returns
        -------
        str
            Error message or None
        """
        err_list = []

        if answer is None:
            err_list.append("[Error] answer is none")
        elif len(answer) < 2:
            err_list.append(
                f"[Error] answer length is small. len:{len(answer)} (< 2)")
        else:
            is_error = False

            # もとの文字列と一致するかチェック
            text2 = ''.join(answer)
            if text2 != quiz:
                is_error = True
                err_list.append("[Error] the string is different")
                err_list.append(f"> actual  :{text2}")
                err_list.append(f"> expected:{quiz}")

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

        if 0 < len(err_list):
            return "\n".join(err_list)
        else:
            return None
