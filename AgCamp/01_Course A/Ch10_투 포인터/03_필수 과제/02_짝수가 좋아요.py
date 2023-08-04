n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)  # index error 때문에 n + 1번째 원소 추가

s, e = 0, 0
cnt = arr[0] % 2

length = 0

while e < n:
    if cnt <= k:
        if length < e - s + 1 - cnt:
            length = e - s + 1 - cnt

        e += 1
        cnt += arr[e] % 2
    else:
        cnt -= arr[s] % 2
        s += 1

print(length)