n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0
s, e = 0, n - 1

while s < e:
  if arr[s] + arr[e] == k:
    cnt += 1
    s += 1
    e -= 1
  elif arr[s] + arr[e] < k:
    s += 1
  else:
    e -= 1

print(cnt)