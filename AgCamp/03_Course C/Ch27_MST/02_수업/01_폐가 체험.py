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


n = int(input())
v = []
par = [0 for i in range(1010)]  # 유니온파인드 만들기
arr = [[0, 0] for i in range(1010)]  # 사람의 좌표 저장

for i in range(n):
    x, y = map(int, input().split())
    arr[i][0], arr[i][1] = x, y

for i in range(n):
    for j in range(i + 1, n):
        dx = arr[i][0] - arr[j][0]
        dy = arr[i][1] - arr[j][1]

        dist = (dx * dx) + (dy * dy)
        v.append((dist, (i, j)))

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
    ans = max(ans, c)

print(ans)