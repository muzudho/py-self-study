"""
python -m tests.nonnumsv_test -m src.nonnumsv.o1o0g1o3o0 -c NonNumSVO1o0g1o3o0
"""


class NonNumSVO1o0g1o3o0:
    """Non-numeric separated value"""

    @staticmethod
    def parse(text):
        return ["ABC", "123", "DEF", "456", "GHI"]
