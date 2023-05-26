n, k = map(int, input().split())

answer = 0

# 내 풀이
while n != 1:
    if n % k == 0:
        n /= k
        answer += 1
    else:
        n -= 1
        answer += 1


# 답안 1) 단순하게 풀기
# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N - 1
    while n % k != 0:
        n -= 1
        answer += 1
    # K로 나누기
    n //= k
    answer += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    answer += 1


# 답안 2) 더 빠르게 동작하는 풀이
while True:
    # N == K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    answer += (n - target)
    n = answer

    # N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    answer += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
answer += (n - 1)

print(answer)