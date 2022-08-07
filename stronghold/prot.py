from Bio.Seq import *

with open('rosalind.in', 'r') as fi, open('rosalind.out', 'w') as fo:
    seq = fi.read()
    fo.write(str(Seq(seq).translate()))