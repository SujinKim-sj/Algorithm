# 병합정렬
def sort(s, e):
    mid = (s + e) // 2
    l, r = 0, 0
    idx = 0

    if s >= e:
        return

    sort(s, mid)
    sort(mid + 1, e)

    l, r = s, mid + 1

    while l <= mid and r <= e:
        if arr[l] < arr[r]:
            tmp[idx] = arr[l]
            idx += 1
            l += 1
        else:
            tmp[idx] = arr[r]
            idx += 1
            r += 1

    while l <= mid:
        tmp[idx] = arr[l]
        idx += 1
        l += 1

    while r <= e:
        tmp[idx] = arr[r]
        idx += 1
        r += 1

    for i in range(idx):
        arr[s + i] = tmp[i]


n = int(input())
arr = list(map(int, input().split()))
tmp = [0] * 100010

sort(0, n - 1)

for i in range(n):
    print(arr[i], end=" ")