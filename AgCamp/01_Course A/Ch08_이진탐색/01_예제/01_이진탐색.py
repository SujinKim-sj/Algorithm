n, q = map(int, input().split())

arr = list(map(int, input().split()))
q_arr = list(map(int, input().split()))

for i in range(q):
    x = q_arr[i]
    s = 0
    e = n - 1
    found = False

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == x:
            found = True
            break
        elif arr[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    if found:
        print("YES")
    else:
        print("NO")