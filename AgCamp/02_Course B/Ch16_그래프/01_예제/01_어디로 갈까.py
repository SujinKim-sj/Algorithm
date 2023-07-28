n, m = map(int, input().split())
v = [[0] for i in range(100010)]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for i in range(1, n + 1):
    v[i].sort()

for i in range(1, n + 1):
    print(len(v[i]) - 1, end=" ")
    for j in range(1, len(v[i])):
        print(v[i][j], end=" ")
    print("")