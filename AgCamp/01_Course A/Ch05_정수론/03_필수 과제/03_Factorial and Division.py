n, a = map(int, input().split())

answer = 0
i = a
while i <= n:
  answer += n // i
  i *= a

print(answer)