n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
  for j in range(m - 1, -1, -1):
    print(arr[i][j], end=" ")
  print("")