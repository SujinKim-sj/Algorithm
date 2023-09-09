import sys

sys.setrecursionlimit(10 ** 6)


def dfs(cur):
    global cnt
    #cnt = len(vec[cur])
    visited[cur] = True

    for i in range(1, len(vec[cur])):
        if visited[vec[cur][i]]:
            continue
        cnt += len(vec[vec[cur][i]])
        dfs(vec[cur][i])


def dfs2(cur):
    global cnt
    #cnt = len(vec2[cur])
    visited[cur] = True

    for i in range(1, len(vec2[cur])):
        if visited[vec2[cur][i]]:
            continue
        cnt += len(vec2[vec2[cur][i]])
        dfs2(vec2[cur][i])


n, m = map(int, input().split())
visited = [False for i in range(110)]

vec = [[0] for i in range(110)]
vec2 = [[0] for i in range(110)]

for i in range(m):
    v1, v2 = map(int, input().split())
    vec[v1].append(v2)  # 가벼운거
    vec2[v2].append(v1)  # 무거운거

# 연결 요소의 개수 구하기
answer = 0

for i in range(1, n + 1):
    visited = [False for i in range(110)]
    cnt = len(vec[i])
    dfs(i)
    if cnt >= (n + 1) // 2:
        answer += 1

for i in range(1, n + 1):
    # print(vec2[i])
    visited = [False for i in range(110)]
    cnt = len(vec2[i])
    dfs2(i)
    if cnt >= (n + 1) // 2:
        answer += 1

print(answer)