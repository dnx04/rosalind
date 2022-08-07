from Bio import SeqIO
from Bio.Seq import Seq

fo = open("output.txt", "w+")

s = list(SeqIO.parse('input.txt', 'fasta'))[0]
s = str(s.seq)

for i in range(len(s)):
  for j in range(i, len(s)):
    if 4 <= j - i + 1 <= 12 and Seq(s[i:j + 1]) == Seq(s[i:j + 1]).reverse_complement():
      print(i + 1, j - i + 1, file=fo)