n, h = map(int, input().split())
delta = [0 for i in range(500010)]
prefix = [0 for i in range(500010)]

for i in range(n):
    a = int(input())

    if i % 2 == 0:  # 아랫쪽
        delta[1] += 1
        delta[a + 1] -= 1
    else:  # 위쪽
        delta[h - a + 1] += 1
        delta[h + 1] -= 1

for i in range(1, h + 1):
    prefix[i] = prefix[i - 1] + delta[i]

mn = 10000000
for i in range(1, h + 1):
    mn = min(mn, prefix[i])

cnt = 0
for i in range(1, h + 1):
    if prefix[i] == mn:
        cnt += 1

print(mn, cnt)