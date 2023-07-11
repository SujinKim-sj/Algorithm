n, m = map(int, input().split())

cnt = 1
for i in range(n, m + 1):
  if cnt % 8 == 0:
    print(i)
  else:
    print(i, end=" ")
  cnt += 1