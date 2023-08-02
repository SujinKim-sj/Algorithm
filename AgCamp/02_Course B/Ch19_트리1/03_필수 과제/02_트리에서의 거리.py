import sys
sys.setrecursionlimit(10 ** 6)

def dfs(cur, prv):
    for i in range(len(v[cur])):
        if v[cur][i] == prv:
            continue
        depth[v[cur][i]] = depth[cur] + 1
        dfs(v[cur][i], cur)

n, x, y = map(int, input().split())
v = [[] for i in range(1010)]
depth = [0 for i in range(1010)]

for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

dfs(x, -1)  # 루트노드를 x로 변경
print(depth[y])  # x가 루트일 때, 노드 y까지의 깊이