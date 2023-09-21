import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
h = list(map(int, sys.stdin.readline().split()))
h.sort()

sum = 0
answer = 3000000000

for i in range(n):
    for j in range(i + 1, n):
        sum = h[i] + h[j]

        s, e = 0, n - 1
        while s < e:
            if s == i or s == j:
                s += 1
            elif e == i or e == j:
                e -= 1
            else:
                tmp = sum - h[s] - h[e]

                if answer > abs(tmp):
                    answer = abs(tmp)

                if sum < h[s] + h[e]:
                    e -= 1
                elif sum > h[s] + h[e]:
                    s += 1
                else:
                    print(0)
                    exit()

print(answer)