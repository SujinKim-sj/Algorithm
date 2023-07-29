def dfs(cur):
    global cnt
    cnt += 1
    visited[cur] = True

    for i in range(1, len(vc[cur])):
        if visited[vc[cur][i]]:
            continue
        dfs(vc[cur][i])


n = int(input())
m = int(input())
visited = [False for i in range(110)]
vc = [[0] for i in range(110)]
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    vc[a].append(b)
    vc[b].append(a)

dfs(1)
print(cnt - 1)