n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

for i in range(m):
    x = m_arr[i]
    found = False
    s, e = 0, n - 1

    while s <= e:
        mid = (s + e) // 2

        if n_arr[mid] == x:
            found = True
            break
        elif n_arr[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    if found:
        print(1)
    else:
        print(0)