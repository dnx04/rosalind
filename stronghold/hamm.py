def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

s1, s2 = input(), input()
print(hamming_distance(s1, s2))