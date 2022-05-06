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

# 6029 : [기초-값변환] 16진 정수 입력받아 8진수로 출력하기
a = input()
b = int(a, 16)
print('%o' % b)

# 6030 : [기초-값변환] 영문자 1개 입력받아 10진수로 변환하기
n = ord(input())
print(n)

# 6031 : [기초-값변환] 정수 입력받아 유니코드 문자로 변환하기
n = int(input())
n = chr(n)
print(n)

# 6042 : [기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f")) # 풀이1)
print(round(a, 2))      # 풀이2)
