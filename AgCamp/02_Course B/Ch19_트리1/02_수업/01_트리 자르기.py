def dfs(cur):
    if cur == erase:
        return
    sz[cur] = 1
    for i in range(len(v[cur])):
        dfs(v[cur][i])
        sz[cur] += sz[v[cur][i]]


n = int(input())
v = [[] for i in range(60)]
par = list(map(int, input().split()))
sz = [0 for i in range(60)]

for i in range(n):
    x = par[i]
    if x == -1:
        r = i
    else:
        v[x].append(i)
        par[i] = x

erase = int(input())

dfs(r)
cnt = 0
for i in range(n):
    if sz[i] == 1:
        cnt += 1

print(cnt)