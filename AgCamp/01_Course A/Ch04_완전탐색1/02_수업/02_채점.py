t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    score = [0 for i in range(n)]
    for x in range(n):
        score[x] = 0
        for y in range(m):
            score[x] += arr[x][y]

    max_arr = 0
    for x in range(n):
        if max_arr < score[x]:
            max_arr = score[x]

    cnt = 0
    for x in range(n):
        if score[x] == max_arr:
            cnt += 1

    print("#" + str(i + 1), cnt, max_arr)

