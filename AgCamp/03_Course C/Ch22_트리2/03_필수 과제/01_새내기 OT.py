import sys


def recur(cur, sum):
    if cur == n:
        if sum != 0:
            s.add(sum)
        return
    recur(cur + 1, sum + card[cur])
    recur(cur + 1, sum)


input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = 0
for i in card:
    m += i

# 조합
s = set()
recur(0, 0)
print(m - len(s))