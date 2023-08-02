def dfs(cur, prv):
  sz[cur] = 1 # 자기 자신은 1개
  for i in range(len(v[cur])):
    if v[cur][i] == prv:
      continue
    depth[v[cur][i]] = depth[cur] + 1
    dfs(v[cur][i], cur)


n, r = map(int, input().split())
v = [[] for i in range(110)]
depth = [0 for i in range(110)]
sz = [0 for i in range(110)]

for i in range(n - 1):
  a, b = map(int, input().split())
  v[a].append(b)
  v[b].append(a)

dfs(r, -1)
answer = 0
for i in range(n):
  if answer < depth[i]:
    answer = depth[i]

print(answer)