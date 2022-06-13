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
