n = int(input())
i = 2
cnt = 0

while i * i <= n:
  if n % i == 0:
    cnt += 1
  i += 1

if n != 1 and cnt == 0:
  print("YES")
else:
  print("NO")