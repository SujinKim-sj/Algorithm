def recur(cur, cnt):
    global answer
    cnt2 = 0
    possible = False

    if cnt == n:
        cnt2 = 0

        for i in range(m):
            possible = True
            for j in range(k):
                if not combination[arr[i][j]]:
                    possible = False

            if possible:  # 고른 n개 식재료로 가능한 요리면 cnt2 ++
                cnt2 += 1

        if answer < cnt2:
            answer = cnt2
        return

    if cur == 2 * n + 1:
        return

    combination[cur] = True  # 고름
    recur(cur + 1, cnt + 1)

    combination[cur] = False  # 고르지않음
    recur(cur + 1, cnt)


n, m, k = map(int, input().split())
arr = []
combination = [False for i in range(30)]
answer = 0
for i in range(m):
    arr.append(list(map(int, input().split())))

recur(1, 0)
print(answer)