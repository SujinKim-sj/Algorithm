n, k = map(int, input().split())
arr = [0] * 100010
arr2 = list(map(int, input().split()))

for i in range(n):
    arr[i] = arr2[i]

s, e = 0, 0
sum = arr[0]
cnt = 0

while e < n:
    if sum == k:
        cnt += 1

    if sum >= k:
        sum -= arr[s]
        s += 1
    else:
        e += 1
        sum += arr[e]

print(cnt)