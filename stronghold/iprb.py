k, m, n = map(int, input().split())

tot = (k + m + n) * (k + m + n - 1) / 2

print((k * ((k - 1) / 2 + m + n) + m * (m - 1) * 0.375 + m * n / 2) / tot)