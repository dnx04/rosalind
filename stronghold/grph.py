from Bio import SeqIO
from Bio.Seq import *
from Bio.SeqUtils import GC

ls = list(SeqIO.parse('rosalind.in', 'fasta'))
fo = open('rosalind.out', 'w+')

for u in ls:
    for v in ls:
        if u.id != v.id and u.seq.endswith(v.seq[0:3]):
            fo.writelines(u.id + ' ' + v.id + '\n')
