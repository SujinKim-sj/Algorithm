test = int(input())

for t in range(test):
    cnt = [0] * 10  # 카운트 배열 초기화
    n = int(input())
    i = n
    counted = True

    while True:
        x = i

        # x 분해해서 카운트
        while x > 0:
            cnt[x % 10] += 1
            x //= 10

        counted = True
        for j in range(10):
            if cnt[j] == 0:
                counted = False

        if counted:
            print("#" + str(t + 1), i)
            break

        i += n