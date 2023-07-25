from collections import deque

n, k = map(int, input().split())
q = deque()

for i in range(1, n + 1):
    q.append(i)

for i in range(n - 1):
    for j in range(k - 1):
        q.append(q.popleft())

    x = q.popleft()

print(x, q.popleft())