import math

is_prime = [False] * 250010
is_prime[1] = False

for i in range(2, 250001):
    is_prime[i] = True

for i in range(2, int(math.sqrt(250000)) + 1):
    if not is_prime[i]:
        continue
    for j in range(i + i, 250000, i):
        is_prime[j] = False

while True:
    n = int(input())
    print(n)
    if n == 0:
      break

    cnt = 0

    for i in range(n + 1, 2 * n + 1):
        if is_prime[i]:
            cnt += 1

    print(cnt)