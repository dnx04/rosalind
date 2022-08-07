from Bio import SeqIO
from Bio.Seq import *
from Bio.SeqUtils import GC

s, max_gc = '', 0
for record in SeqIO.parse('rosalind.in', 'fasta'):
    if(max_gc < GC(record.seq)):
        max_gc = GC(record.seq)
        s = record.id
print(s)
print(max_gc)