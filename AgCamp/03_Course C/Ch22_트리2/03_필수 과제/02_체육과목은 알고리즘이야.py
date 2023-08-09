import sys

sys.setrecursionlimit(10 ** 6)


def dfs(cur):
    global mid
    if cur == -1:  # 자식노드 존재x
        return

    dfs(arr[cur][0])
    mid = cur
    dfs(arr[cur][1])


def count(cur):
    global cnt, mid, answer

    if arr[cur][0] != -1:
        cnt += 1
        count(arr[cur][0])
    if arr[cur][1] != -1:
        cnt += 1
        count(arr[cur][1])

    if cur == mid:  # 순회의 끝이면 시험 끝
        answer = cnt
    cnt += 1


n = int(input())
arr = [[0, 0] for i in range(100010)]

for i in range(n):
    a, b, c = map(int, input().split())
    arr[a][0] = b
    arr[a][1] = c

mid, cnt, answer = 0, 0, 0
dfs(0)
count(0)
print(answer)