x, y, n, m = map(int, input().split())

count = 0
for i in range(1, n):
    for j in range(1, n):
        if i + j == n:
            if x * i + y * j == m:
                count += 1
                uni, gni = i, j

if count == 1:
    print(uni, gni)
else:
    print(-1)
