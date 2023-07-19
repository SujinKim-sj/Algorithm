def check(x):
    sum = 0
    for i in range(n):
        if arr[i] > x:
            sum += arr[i] - x

    return sum >= m


n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
s, e = 0, 1000000000

while s <= e:
    mid = (s + e) // 2

    if check(mid):  # True이면 answer 갱신 저장, 왼쪽 버림
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)