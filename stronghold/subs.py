import re

def count_occ(pattern, string):
    a = [m.start() for m in re.finditer(
        '(?={0})'.format(re.escape(pattern)), string)]
    return a

s, p = input(), input()
for i in map(lambda x: x + 1, count_occ(p, s)):
    print(i, end=' ')