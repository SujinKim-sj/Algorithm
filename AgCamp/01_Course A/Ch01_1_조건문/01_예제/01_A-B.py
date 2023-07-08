a, b = map(int, input().split())

if a - b < 0:
  answer = -1
else:
  answer = a - b

print(answer)