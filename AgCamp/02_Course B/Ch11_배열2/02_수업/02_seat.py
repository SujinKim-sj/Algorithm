r, c = map(int, input().split())
k = int(input())
arr = [[0 for i in range(c + 1)] for i in range(r + 1)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1
d = 0

for i in range(1, r * c + 1):
    arr[x][y] = i

    nx = x + dx[d]
    ny = y + dy[d]

    # 0 1 2 3 0 으로 전환
    if nx < 1 or ny < 1 or nx > r or ny > c or arr[nx][ny] != 0:
        d = (d + 1) % 4

    x = x + dx[d]
    y = y + dy[d]

answer = False

for i in range(1, r + 1):
    for j in range(1, c + 1):
        if arr[i][j] == k:
            answer = True
            print(i, j)

if not answer:
    print(0)