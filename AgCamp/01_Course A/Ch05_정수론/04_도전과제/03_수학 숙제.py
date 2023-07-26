import sys


# 최대공약수
def gcd_a(x, y):
    while y % x != 0:
        z = y % x
        y = x
        x = z
    return x


a, d = map(int, sys.stdin.readline().split())  # 초항, 공차
q = int(input())  # 문제의 개수

for i in range(q):
    op, l, r = map(int, sys.stdin.readline().split())
    sum = 0
    if op == 1:
        x = a + (l - 1) * d
        y = a + (r - 1) * d
        n = r - l + 1
        sum = n * (x + y) // 2  # 합 : 등차수열의 합 공식을 활용

        print(sum)
    else:
        if l == r:
            print(a + (l - 1) * d)
        else:
            print(gcd_a(a, d))

# HINT
# 등차수열의 합을 구하는 과정에서 주어질 수 있는 r번째 항의 범위가 100만이기 때문에
# 반복문을 이용해 각 항을 하나씩 더해주는것 보다는
# 등차수열의 합 공식을 활용하여 계산하시면 시간 단축에 도움이 될 거에요!!