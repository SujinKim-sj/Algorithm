import sys

sys.setrecursionlimit(10 ** 6)


def dfs(cur, color):
    global flag
    visited[cur] = color

    for i in range(len(v[cur])):
        if visited[v[cur][i]] == color:  # 2색칠하기 불가능
            flag = 1
            return
        if visited[v[cur][i]] == 0:
            dfs(v[cur][i], color * -1)


n, m = map(int, input().split())
visited = [0 for i in range(100010)]
v = [[] for i in range(100010)]
flag = 0

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

dfs(0, 1)

if flag == 1:
    print("NO")
else:
    print("YES")