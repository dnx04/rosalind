inp = input()
table = inp.maketrans('ATCG', 'TAGC')
print(inp.translate(table)[::-1])