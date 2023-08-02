n, x, y = map(int, input().split())
par = [0 for i in range(1005)] # 부모노드
color = [False for i in range(1005)]

for i in range(n - 1):
  a, b = map(int, input().split())
  par[b] = a

while True:
  color[x] = True
  if x == 0:
    break
  x = par[x]

print(color)
while True:
  if color[y]:
    print(y)
    break
  color[y] = True
  y = par[y]