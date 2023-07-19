test = int(input())
for i in range(test):
    t = int(input())

    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0

    for i in range(t):
        for j in range(i + 1, t):
            s, e = i, j
            found = False

            if abs(s - e) != 1:
                mid = (s + e) // 2
                if abs(arr[s] - arr[mid]) == abs(arr[e] - arr[mid]):
                    found = True
                    print(arr[s], arr[mid], arr[e])
                    cnt += 1

    print(cnt)