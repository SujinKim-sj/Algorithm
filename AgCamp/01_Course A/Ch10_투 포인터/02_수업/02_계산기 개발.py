n, k = map(int, input().split())
arr = [0] * 100010
arr2 = list(map(int, input().split()))

for i in range(n):
    arr[i] = arr2[i]

s, e = 0, 0
sum = arr[0]
mn = 100000000  # 최소의 길이

while e < n:
    if sum >= k:
        if mn > e - s + 1:  # 길이 갱신
            mn = e - s + 1

        sum -= arr[s]
        s += 1
    else:
        e += 1
        sum += arr[e]

if mn == 100000000:
    mn = 0

print(mn)