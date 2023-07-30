n = int(input())
cnt = 0

# 제곱수 찾기
i = 1
while i * i <= n:
  cnt += 1
  i += 1

print(cnt)