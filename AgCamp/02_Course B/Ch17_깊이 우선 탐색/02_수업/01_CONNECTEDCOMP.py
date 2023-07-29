import sys
sys.setrecursionlimit(10 ** 6)

def dfs(cur):
    visited[cur] = True

    for i in range(1, len(vec[cur])):
        if visited[vec[cur][i]]:
            continue
        dfs(vec[cur][i])


v, e = map(int, input().split())
cnt = 0
visited = [False for i in range(1010)]
vec = [[0] for i in range(1010)]

for i in range(e):
    v1, v2 = map(int, input().split())
    vec[v1].append(v2)
    vec[v2].append(v1)

# 연결 요소의 개수 구하기
for i in range(1, v + 1):
    if visited[i]:
        continue
    dfs(i)
    cnt += 1

print(cnt)