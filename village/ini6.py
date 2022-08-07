mp = {}

for word in input().split():
    mp[word] = mp.get(word, 0) + 1

for k, v in mp.items():
    print(k, v)