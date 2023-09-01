def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    par[a] = b


n, m = map(int, input().split())
v = []
par = [0 for i in range(10010)]  # 유니온파인드 만들기

for i in range(m):
    a, b, c = map(int, input().split())
    v.append((c, (a, b)))

v.sort()

for i in range(n):
    par[i] = i

ans = 0  # 가중치 합
for i in range(len(v)):
    a = find(v[i][1][0])
    b = find(v[i][1][1])
    c = v[i][0]

    if a == b:
        continue
    union_(a, b)
    ans += c

print(ans)