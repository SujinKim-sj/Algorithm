t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    max_arr = -1

    for j in range(n):
        for k in range(j + 1, n):
            if arr[j] + arr[k] <= m:
                if max_arr < arr[j] + arr[k]:
                    max_arr = arr[j] + arr[k]

    print("#" + str(i + 1), max_arr)
