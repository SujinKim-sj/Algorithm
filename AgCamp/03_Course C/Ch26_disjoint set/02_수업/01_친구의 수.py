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

    sz[b] += sz[a]
    par[a] = b


n, q = map(int, input().split())
par = [i for i in range(1000010)]
sz = [1 for i in range(1000010)]

for _ in range(q):
    arr = list(map(int, input().split()))
    a = arr[0]
    if a == 0:
        b, c = arr[1], arr[2]
        union_(b, c)
    else:
        b = arr[1]
        print(sz[find(b)])