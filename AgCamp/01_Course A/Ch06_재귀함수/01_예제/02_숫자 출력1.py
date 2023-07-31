def num_print(cur):
    if cur == n:
        for j in range(n):
            print(arr[j], end='')
        print('')
        return

    for i in range(m):
        arr[cur] = i
        num_print(cur + 1)


# n자리 m진수
n, m = map(int, input().split())
arr = [0] * 50
num_print(0)
