import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def find(x):
    if par[x] == x:
        return x
    else:  # 최적화(경로 압축)
        par[x] = find(par[x])
        return par[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    par[a] = b


n, q = map(int, input().split())
par = [i for i in range(1000010)]

for _ in range(q):
    a, b, c = map(int, input().split())

    if a == 0:
        union_(b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")
