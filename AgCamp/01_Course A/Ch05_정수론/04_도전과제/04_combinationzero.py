# 1. n!을 소인수분해했을 때 2의 개수, 5의 개수를 구한다.
# 2. (n-m)!과 m!에 대해서도 연산한다.
# 3. 지수법칙에 근거하여 nCm의 2의 개수와 5의 개수를 구한다.
def count_num(num, x):
  cnt = 0
  while num > 0:
    cnt += num // x
    num //= x

  return cnt

  # two, five = 0, 0
  # for i in range(1, num + 1):
  #   while i % 2 == 0:
  #     two += 1
  #     i //= 2
  #
  #   while i % 5 == 0:
  #     five += 1
  #     i //= 5
  #   # print(two, five)
  #
  # return two, five


n, m = map(int, input().split())

# n!의 2와 5의 개수
t1, f1 = count_num(n, 2), count_num(n, 5)

# n - m !과 m!의 2와 5의 개수
t2, f2 = count_num(m, 2), count_num(m, 5)
t3, f3 = count_num(n - m, 2), count_num(n - m, 5)

t = t1 - t2 - t3
f = f1 - f2 - f3

answer = min(t, f)
print(answer)





