n = int(input()) # A의 길이
b = list(map(int, input().split()))

tmp = 0
for i in range(n):
  value = b[i] * (i + 1) - tmp
  tmp += value
  print(value, end=" ")