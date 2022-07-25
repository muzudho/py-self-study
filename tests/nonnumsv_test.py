"""
python -m tests.nonnumsv_test -m src.nonnumsv
"""
from src.nonnumsv import NonNumSV

vec = NonNumSV.parse("ABC123DEF456GHI")

vec_size = len(vec)
if vec_size == 5:
    print("size is ok")
else:
    print(f"[Error] the size is different. size:{vec_size}")

if vec == ["ABC", "123", "DEF", "456", "GHI"]:
    print("correct!")
else:
    print(f"[Error] the response is different. vec:{vec}")
