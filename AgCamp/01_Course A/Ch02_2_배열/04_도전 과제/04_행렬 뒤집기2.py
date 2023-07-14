n = int(input())
arr = [[0 for i in range(20)] for j in range(20)]
input_arr = [list(map(int, input().split())) for i in range(10)]  # 행렬 입력받기

for i in range(1, 11):
    for j in range(1, 11):
        arr[i][j] = input_arr[i - 1][j - 1]

for i in range(1, n + 1):
    for j in range(1, 11):
        if arr[i][j] == 1:
            arr[i][j] = 0
        else:
            arr[i][j] = 1

    for j in range(1, 11):
        if arr[j][i] == 1:
            arr[j][i] = 0
        else:
            arr[j][i] = 1

    if arr[i][i] == 1:
        arr[i][i] = 0
    else:
        arr[i][i] = 1

# 뒤집기 게임 후 출력
for i in range(1, 11):
    for j in range(1, 11):
        print(arr[i][j], end=" ")
    print("")