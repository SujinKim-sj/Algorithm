n = int(input())
t = list(map(int, input().split()))
g = list(map(int, input().split()))
answer = 0

for i in range(n):
  answer += t[i]

g.sort()

for i in range(n):
  answer += i * g[i]

print(answer)