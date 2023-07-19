n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for i in range(q):
    x = int(input())
    s = 0
    e = n - 1

    ans = -1

    while s <= e:
        mid = (s + e) // 2
        if arr[mid] >= x:  # x보다 크거나 같으면 mid 를 정답후보, mid 이상은 제거
            ans = mid
            e = mid - 1
        else:  # x보다 작으면 mid 이하는 제거
            s = mid + 1

    print(ans)