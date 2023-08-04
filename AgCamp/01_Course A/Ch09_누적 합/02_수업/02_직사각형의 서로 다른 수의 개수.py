n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
prefix = [[[0 for i in range(20)] for i in range(310)] for i in range(310)]  # 3차원 배열

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, 11):
            prefix[i][j][k] = prefix[i][j - 1][k] + prefix[i - 1][j][k] - prefix[i - 1][j - 1][k]

        prefix[i][j][arr[i - 1][j - 1]] += 1  # 현재 값 추가

q = int(input())
while q > 0:
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    for i in range(1, 11):  # 0 이 아니면 cnt + 1을 해준다
        if prefix[x2][y2][i] - prefix[x2][y1 - 1][i] - prefix[x1 - 1][y2][i] + prefix[x1 - 1][y1 - 1][i] != 0:
            cnt += 1
    q -= 1

    print(cnt)