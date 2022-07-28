class Questioner:
    """出題者"""

    def make_quiz(self):
        """答えのある問い作成"""
        return "ABC123DEF456GHI"

    def check(self, answer, quiz):
        """答え合わせ"""

        if answer is None:
            print("[Error] vec is none")
        else:
            vec_size = len(answer)
            if vec_size == 5:
                print("size is ok")
            else:
                print(f"[Error] the size is different. size:{vec_size}")

            if answer == ["ABC", "123", "DEF", "456", "GHI"]:
                print("correct!")
            else:
                print(f"[Error] the response is different. vec:{answer}")
