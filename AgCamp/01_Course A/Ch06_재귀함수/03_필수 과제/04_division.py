def division(sum, idx):
    global cnt
    # 현재까지 구한 합이 sum, idx 번째 숫자를 결정할 차례
    if sum == n:
        for i in range(idx):
            if i == idx - 1:
                print(result[i], end="")
            else:
                print(result[i], end="+")
        print("")
        cnt += 1
    else:
        if idx == 0:
            num = n - 1
        else:
            num = n - sum

        for i in range(num, 0, -1):
            result[idx] = i

            # 중복 제거
            if idx > 0 and result[idx - 1] < result[idx]:
                continue
            division(sum + i, idx + 1)


n = int(input())
result = [0] * 30
cnt = 0

division(0, 0)
print(cnt)