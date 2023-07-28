n, q = map(int, input().split())
v = [[0 for i in range(1010)] for i in range(1010)]
cnt = [0 for i in range(1010)]

for i in range(q):
    info = list(map(int, input().split()))

    if info[0] == 1:  # 간선 연결,삭제
        a, b = info[1], info[2]

        if v[a][b] == 1:
            v[a][b] = 0
            v[b][a] = 0

            cnt[a] -= 1
            cnt[b] -= 1
        else:
            v[a][b] = 1
            v[b][a] = 1

            cnt[a] += 1
            cnt[b] += 1
    else:
        a = info[1]
        print(cnt[a])  # a에 연결된 간선 개수 출력