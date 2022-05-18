# 파이썬 기초 100제
# 기초 - 3

# 6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기
a, b = input().split()
a = int(a)
b = int(b)
c = a if (a >= b) else b
print(int(c))

# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
min = a if a < b else b
min = c if c < min else min
print(int(min))
