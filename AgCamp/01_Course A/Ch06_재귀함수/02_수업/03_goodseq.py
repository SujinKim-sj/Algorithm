def check(x, length):
    # arr[x] 가 오른쪽 끝이고, 길이의 중복이 있는지 판별
    # 중복이 없다면 true, 아니면 False
    for i in range(length):
        if arr[x - i] != arr[x - i - length]:
            return True

    return False


def goodseq(x):
    global printed
    if printed:  # 첫 번째 수열 출력
        return
    if x >= n:
        for i in range(n):
            print(arr[i], end="")
        print("")
        printed = True
        return

    for i in range(1, 4):
        arr[x] = i

        flag = False
        for j in range(1, (x + 1) // 2 + 1):
            if check(x, j) == False:
                flag = True
                break

        if flag == False:
            goodseq(x + 1)


n = int(input())
arr = [0] * 110
printed = False
goodseq(0)