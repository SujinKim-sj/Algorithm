def dfs(cur, prv):
    for i in range(len(v[cur])):
        if v[cur][i] == prv:
            continue
        depth[v[cur][i]] = depth[cur] + 1

        dfs(v[cur][i], cur)


n, k = map(int, input().split())
v = [[] for i in range(100010)]
depth = [0 for i in range(100010)]

for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

berry = list(map(int, input().split()))

dfs(0, -1)
answer = 0
for i in range(n):
    if depth[i] <= k:
        answer += berry[i]

print(answer)