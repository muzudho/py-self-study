"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o5o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o4o0 --ac NonNumSV
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
