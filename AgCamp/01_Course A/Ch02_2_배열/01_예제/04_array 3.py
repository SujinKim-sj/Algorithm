n = int(input())
num = 1
arr = [[0 for i in range(110)] for j in range(110)]

for i in range(n):
    x = 0
    y = i

    for j in range(i + 1):
        arr[x][y] = num
        num += 1

        x += 1
        y -= 1

for i in range(n):
    for j in range(n - i):
        print(arr[i][j], end=" ")
    print("")
