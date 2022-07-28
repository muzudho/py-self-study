"""
python -m tests.nonnumsv.o1o0g1o1o0.test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSV
"""
import re


class NonNumSV:
    """Non-numeric separated value"""

    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def to_answer(text):
        m = NonNumSV.__pat.match(text)
        if m:
            return [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]

        return None
