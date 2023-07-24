n = int(input())
info = list(map(str, input().split()))

if n > 32:
    answer = 0
else:
    # 세 개의 사료를 고르기
    answer = 100000
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                count = []
                cnt = 0
                if info[i][0] != info[j][0]:
                    cnt += 1
                if info[i][1] != info[j][1]:
                    cnt += 1
                if info[i][2] != info[j][2]:
                    cnt += 1
                if info[i][3] != info[j][3]:
                    cnt += 1
                count.append(cnt)

                cnt = 0
                if info[i][0] != info[k][0]:
                    cnt += 1
                if info[i][1] != info[k][1]:
                    cnt += 1
                if info[i][2] != info[k][2]:
                    cnt += 1
                if info[i][3] != info[k][3]:
                    cnt += 1
                count.append(cnt)

                cnt = 0
                if info[j][0] != info[k][0]:
                    cnt += 1
                if info[j][1] != info[k][1]:
                    cnt += 1
                if info[j][2] != info[k][2]:
                    cnt += 1
                if info[j][3] != info[k][3]:
                    cnt += 1
                count.append(cnt)

                answer = min(answer, sum(count))

print(answer)