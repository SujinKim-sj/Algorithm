# 파이썬 기초 100제
# 기초 - 값 변환, 출력 변환

# 6025 : [기초-값변환] 정수 2개 입력받아 합 계산하기
a, b = input().split()
c = int(a) + int(b)
print(c)

# 6026 : [기초-값변환] 실수 2개 입력받아 합 계산하기
a = input()
b = input()
c = float(a) + float(b)
print(c)

# 6027 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기1
a = input()
b = int(a)
print('%x' % b)

# 6028 : [기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
a = input()
b = int(a)
print('%X' % b)
