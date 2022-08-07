from Bio.Seq import *

with open('rosalind.in', 'r') as fi:
    s = fi.read()
    print(Seq(s).count('A'), Seq(s).count('C'), Seq(s).count('G'), Seq(s).count('T'))