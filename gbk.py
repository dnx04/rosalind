from Bio import Entrez

def genbank(query, start, end):
  Entrez.email = 'lmao@lmao.com'
  term = '%s[Organism] AND (%s[Publication Date] : %s[Publication Date])' % (query, start, end)
  handle = Entrez.esearch(db="nucleotide", term=term)
  record = Entrez.read(handle)
  return record["Count"]

q, s, f = input(), input(), input()
print(genbank(q, s, f))