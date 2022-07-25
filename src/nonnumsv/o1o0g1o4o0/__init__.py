"""
python -m tests.nonnumsv_test -m src.nonnumsv.o1o0g1o4o0 -c NonNumSVO1o0g1o4o0
"""
import re


class NonNumSVO1o0g1o4o0:
    """Non-numeric separated value"""

    __pat = re.compile(r"^([A-Z]+)([0-9]+)([A-Z]+)([0-9]+)([A-Z]+)$")

    @staticmethod
    def parse(text):
        m = NonNumSVO1o0g1o4o0.__pat.match(text)
        if m:
            return [m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)]

        return None
