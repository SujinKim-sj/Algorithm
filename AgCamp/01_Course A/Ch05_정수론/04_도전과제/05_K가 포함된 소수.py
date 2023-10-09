# 파이썬 시간초과 PASS
import sys

sys.setrecursionlimit(10 ** 6)
test = int(input())

# 소수 구하기
is_prime = [True] * 10000001
j = 2
while j * j <= 10000001:
    if is_prime[j] == True:
        for k in range(j + j, 1000001, j):
            is_prime[k] = False
    j += 1

for t in range(test):
    print("#" + str(t + 1), end=" ")
    v, s, e = map(int, input().split())
    count = 0

    for i in range(s, e + 1):
        if is_prime[i]:
            # 소수 이고 v가 포함된 숫자 세기
            si = str(i)
            for j in range(len(si)):
                if si[j] == str(v):
                    count += 1

    print(count)