"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o3o0 --ac Answerer
"""


class Answerer:
    """Non-numeric separated value"""

    @staticmethod
    def to_answer(text):
        return ["ABC", "123", "DEF", "456", "GHI"]
