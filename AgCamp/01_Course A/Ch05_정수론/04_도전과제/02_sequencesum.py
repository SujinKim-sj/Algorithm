n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
a = [0] * n

for i in range(n):
    if i == 0:
        a[i] = (s[i][1] + s[i][2] - s[1][2]) // 2
    else:
        a[i] = s[i - 1][i] - a[i - 1]

    print(a[i], end=" ")