from Bio.Seq import Seq

s, p = input(), input()
print(Seq(s).count_overlap(p))