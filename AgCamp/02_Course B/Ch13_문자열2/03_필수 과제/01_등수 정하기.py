n = int(input())
arr = [list(map(str, input().split())) for i in range(3)]
cnt = {}
count = 0
score = [0 for i in range(3)]

for i in range(3):
    for j in range(n):
        if arr[i][j] in cnt:
            cnt[arr[i][j]] += 1
        else:
            cnt[arr[i][j]] = 1

for i in range(3):
    for j in range(n):
        if cnt[arr[i][j]] == 1:
            score[i] += 3
        elif cnt[arr[i][j]] == 2:
            score[i] += 1

    print(score[i], end=" ")