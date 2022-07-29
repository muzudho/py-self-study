class Questioner:
    """出題者"""

    def make_quiz(self):
        """答えのある問い作成"""
        return "ABC123DEF456GHI"

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
        else:
            vec_size = len(answer)
            if vec_size != 5:
                err_list.append(
                    f"[Error] the size is different. size:{vec_size}")

            if answer != ["ABC", "123", "DEF", "456", "GHI"]:
                err_list.append(
                    f"[Error] the response is different. vec:{answer}")

        if 0 < len(err_list):
            return "\n".join(err_list)
        else:
            return None
