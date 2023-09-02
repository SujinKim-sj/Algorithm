n, k = map(int, input().split())
arr = [0 for i in range(200010)]
arr2 = list(map(int, input().split()))

for i in range(1, n + 1):
  arr[i] = arr2[i - 1]

prefix = [0 for i in range(200010)]

for i in range(1, n + 1):
  prefix[i] = prefix[i - 1] + arr[i]

ans = 0
cnt = dict.fromkeys(prefix, 0)

for i in range(n + 1):
  if prefix[i] - k in cnt:
    ans += cnt[prefix[i] - k]
  if prefix[i] in cnt:
    cnt[prefix[i]] += 1

print(ans)