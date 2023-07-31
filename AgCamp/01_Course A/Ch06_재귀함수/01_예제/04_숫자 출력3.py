def num_print(cur, start):
    if cur == n:
        for j in range(n):
            print(arr[j], end='')
        print('')
        return

    for i in range(start, m):
        arr[cur] = i
        num_print(cur + 1, i + 1)


# n자리 m진수
n, m = map(int, input().split())
arr = [0] * 50

num_print(0, 0)