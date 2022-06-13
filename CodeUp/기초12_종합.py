# 파이썬 기초 100제
# 기초 - 종합

# 6077 : [기초-종합] 짝수 합 구하기
n = int(input())
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i

print(sum)

# 6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기
c = 'a'
while c != 'q':
    c = input()
    print(c)
    
# 6079 : [기초-종합] 언제까지 더해야 할까?
n = int(input())
i = 1
sum = 0

while True:
    sum += i
    if sum >= n:
        print(i)
        break
    else:
        i += 1


# 6080 : [기초-종합] 주사위 2개 던지기
n, m = input().split()
n = int(n)
m = int(m)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)
        
        
# 6081 : [기초-종합] 16진수 구구단 출력하기
n = input()
n = int(n, 16)

for i in range(1, int('F', 16) + 1):
    print('%X'%n, '*%X'%i, '=%X'%(n * i), sep='')

# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자
n = int(input())

for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')
        
        
# 6083 : [기초-종합] 빛 섞어 색 만들기
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
sum = 0

for i in range(r):
  for j in range(g):
    for k in range(b):
        print(i, j, k)
        sum += 1

print(sum)

# 6084 : [기초-종합] 소리 파일 저장용량 계산하기
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

pcm = h * b * c * s / 8 / 1024 / 1024
print(round(float(pcm), 1), 'MB')


# 6085 : [기초-종합] 그림 파일 저장용량 계산하기
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)

save = w * h * b / 8 / 1024 / 1024

print('%.2f'%save, "MB")

# 6086 : [기초-종합] 거기까지! 이제 그만~
n = int(input())
i = 1
sum = 0
while True:
    sum += i
    i += 1
    if sum >= n:
        break
        
print(sum)

# 6087 : [기초-종합] 3의 배수는 통과
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print(i, end=' ')

# 6088 : [기초-종합] 수 나열하기1
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

for i in range(n - 1):
    a += d
print(a)

# 6089 : [기초-종합] 수 나열하기2
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

for i in range(n - 1):
    a *= r
print(a)

# 6090 : [기초-종합] 수 나열하기3
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n):
    a = a * m + d
print(a)

# 6091 : [기초-종합] 함께 문제 푸는 날
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
  d += 1
print(d)
