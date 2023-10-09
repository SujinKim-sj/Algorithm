def to_k_num(n, k):  # n을 k진수로 바꾸기
    s = ''
    while n > 0:
        n, mod = divmod(n, k)
        s += str(mod)

    return s[::-1]


def is_prime_num(k):  # 소수 개수 구하기
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 3:
        return False

    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False

    return True


n, k = map(int, input().split())
answer = 0

new_num = to_k_num(n, k)

# 0 기준으로 수 나누기
for i in new_num.split('0'):
    if i == '':
        continue
    if is_prime_num(int(i)):
        answer += 1

print(answer)