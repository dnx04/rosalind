from Bio.Seq import Seq

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
s = Seq(fi.read())
fo.write(str(s.reverse_complement()))