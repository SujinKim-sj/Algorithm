arr = list(map(int, input().split()))
answer = 1000001
# 1) 100만까지 중 나누어 떨어지는 수 구하기
for i in range(1, 1000001):
  cnt = 0
  for j in range(5):
    if i % arr[j] == 0:
      cnt += 1

  if cnt >= 3:
    answer = min(answer, i)

print(answer)
# 2) 주어진 수 중 3개 뽑아서 나누어 떨어지는 수 구하기
# 유클리드 호제법 사용하면 더 빠름, but 조건이 크지 않기 때문에 아래처럼해도 시간 초과되지 않는다
answer2 = 1000001
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            for l in range(1, 1000001):
                if l % arr[i] == 0 and l % arr[j] == 0 and l % arr[k] == 0:
                    answer2 = min(answer2, l)

print(answer2)