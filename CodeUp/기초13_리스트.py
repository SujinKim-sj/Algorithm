# 파이썬 기초 100제
# 기초 - 리스트

# 6092 : [기초-리스트] 이상한 출석 번호 부르기1
  
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')


# 6093 : [기초-리스트] 이상한 출석 번호 부르기2
  
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n - 1, -1, -1):
    print(a[i], end=" ")
    
    
# 6094 : [기초-리스트] 이상한 출석 번호 부르기3  

n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

min = a[0]
for i in range(n):
    if min > a[i]:
        min = a[i]

print(min)


# 6095 : [기초-리스트] 바둑판에 흰 돌 놓기

d = [[0 for j in range(20)] for i in range(20)]
n = int(input())

for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()

# 6096 : [기초-리스트] 바둑알 십자 뒤집기

d = [[0 for j in range(20)] for i in range(20)]
for i in range(19):
    a = input().split()
    for j in range(19):
        d[i + 1][j + 1] = int(a[j])

n = int(input())

for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if d[j][int(y)] == 0:
            d[j][int(y)] = 1
        else:
            d[j][int(y)] = 0
        if d[int(x)][j] == 0:
            d[int(x)][j] = 1
        else:
            d[int(x)][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
    
    
# 6097 : [기초-리스트] 설탕과자 뽑기

h, w = input().split()  # 격자판의 세로, 가로
h = int(h)
w = int(w)
n = int(input())    # 막대의 개수

s = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    l, d, x, y = input().split()    # 막대 길이, 방향, 좌표(x, y)
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
   
    for j in range(l):
        if d == 0:  # 가로
            s[x - 1][y - 1 + j] = 1
        else:   # 세로
            s[x - 1 + j][y - 1] = 1


for i in range(h):
    for j in range(w):
        print(s[i][j], end=' ')
    print()


# 6098 : [기초-리스트] 성실한 개미

box = [[] for i in range(10)]

for i in range(10):
    box[i] = list(map(int, input().split()))

x = 1
y = 1

while True:
    if box[x][y] == 2:
        box[x][y] = 9
        break

    if box[x][y + 1] != 1:
        box[x][y] = 9
        y += 1
    else:
        if box[x + 1][y] != 1:
            box[x][y] = 9
            x += 1
        else:
            box[x][y] = 9
            break

for i in range(10):
    for j in range(10):
        print(box[i][j], end=' ')
    print()

