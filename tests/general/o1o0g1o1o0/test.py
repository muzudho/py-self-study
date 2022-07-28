"""
Example
-------
python -m tests.general.o1o0g1o1o0.test --qm tests.nonnumsv.o1o0g1o1o0.quest --qc Questioner --am src.nonnumsv.o1o0g1o2o0 --ac NonNumSV
"""
import argparse
from src.dimport import Dimport  # Dynamic class import

# Command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('--qm', help='questioner module')
ap.add_argument('--qc', help='questioner class')
ap.add_argument('--am', help='answerer module')
ap.add_argument('--ac', help='answerer class')
args = ap.parse_args()

# Plan
Questioner = Dimport.load(args.qm, args.qc)
quest = Questioner()
quiz = quest.make_quiz()
print(f"quiz:{quiz}")

# Do
Answerer = Dimport.load(args.am, args.ac)
answer = Answerer.to_answer(quiz)
print(f"answer:{answer}")

# Check
quest.check(answer, quiz)
