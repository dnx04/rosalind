from Bio import Entrez

def genbank(query):
  Entrez.email = "lmao@lmao.com"
  handle = Entrez.efetch(db="nucleotide", id=query, rettype="fasta")
  records = handle.read()
  return records

ls = genbank(open('input.txt').read().split())
print(ls)
# max_len = 0
# ret = None

# for record in ls:
#   if len(record.seq) > max_len:
#     max_len = len(record.seq)
#     ret = record
    
# print(ret)
