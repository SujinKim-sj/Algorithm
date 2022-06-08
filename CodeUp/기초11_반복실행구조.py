# 파이썬 기초 100제
# 기초 - 반복실행구조

# 6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기

# 주어진 조건식의 평가 결과가 True 인 경우에만, 들여쓰기로 구분된 코드블록이 실행
while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(n)

# 6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1
n = int(input())

while n != 0:
    print(n)
    n = n - 1

# 6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2
n = int(input())

while n != 0:
    n = n - 1
    print(n)
    
# 6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
c = ord(input())
t = ord('a')

while t <= c:
    print(chr(t), end=' ')
    t += 1
      
# 6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1
n = int(input())
s = 0

while s <= n:
    print(s)
    s += 1
    
# 6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2
n = int(input())

for i in range(n + 1):
    print(i)
    
