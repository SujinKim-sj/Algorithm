n, s = map(int, input().split())

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")

    arr = []
    for j in range(2 * i + 1):
        arr.append(s)
        s += 1
        if s > 9:
            s = 1

    for j in range(2 * i + 1):
        if i % 2 == 0:  # 거꾸로 1씩 증가
            print(arr[len(arr) - j - 1], end="")
        else:
            print(arr[j], end="")
    print('')