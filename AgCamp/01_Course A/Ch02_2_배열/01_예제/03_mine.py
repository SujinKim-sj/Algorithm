n, m = map(int, input().split())
x, y = map(int, input().split())

arr = [[0 for i in range(110)] for j in range(110)]
arr2 = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr2[i][j] == 1:
            arr[i + 1][j + 1] = 1

if arr[x][y] == 1:
    print("game over")
else:
    ans = 0  # 1의 합
    ans += arr[x - 1][y - 1]
    ans += arr[x - 1][y]
    ans += arr[x - 1][y + 1]
    ans += arr[x][y - 1]
    ans += arr[x][y + 1]
    ans += arr[x + 1][y - 1]
    ans += arr[x + 1][y]
    ans += arr[x + 1][y + 1]

    print(ans)