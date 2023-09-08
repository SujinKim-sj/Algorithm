test = int(input())

for t in range(test):
    n = int(input())
    bread = list(map(int, input().split()))
    cnt = [0 for i in range(110)]
    x = bread[0]

    for i in range(1, n):
        cnt[bread[i]] += 1

    idx = 0
    for i in range(110):
        if cnt[i] > 0:
            idx = i

    answer = 0
    while x <= idx:
        answer += 1
        x += 1
        cnt[idx] -= 1
        cnt[idx - 1] += 1

        if cnt[idx] == 0:
            idx -= 1

    print("#" + str(t + 1), answer)