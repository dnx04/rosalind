d = {}
s, k = input(), int(input())

for i in range(len(s) - k + 1):
  d[s[i:i+k]] = d.get(s[i:i+k], 0) + 1

pick = max(d, key=d.get)
for key, val in d.items():
  if val == d[pick]:
    print(key)