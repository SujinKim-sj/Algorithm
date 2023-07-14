arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        arr2[i][j] = arr[i][j]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(5):
    for y in range(5):
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < 5 and 0 <= ny < 5:
                if arr[nx][ny] <= arr[x][y]:
                    cnt += 1
            else:
                continue

        if cnt == 0:
            arr2[x][y] = "*"

for i in range(5):
    for j in range(5):
        print(arr2[i][j], end=" ")
    print("")
