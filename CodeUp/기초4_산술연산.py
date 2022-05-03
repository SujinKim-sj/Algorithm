# 파이썬 기초 100제
# 기초 - 산술연산

# 6032 : [기초-산술연산] 정수 1개 입력받아 부호 바꾸기
n = int(input())
print(-n)

# 6033 : [기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기
s = ord(input())
print(chr(s + 1))

# 6034 : [기초-산술연산] 정수 2개 입력받아 차 계산하기
a, b = input().split()
c = int(a) - int(b)
print(c)

# 6035 : [기초-산술연산] 실수 2개 입력받아 곱 계산하기
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

# 6036 : [기초-산술연산] 단어 여러 번 출력하기
w, n = input().split()
print(w * int(n))

# 6037 : [기초-산술연산] 문장 여러 번 출력하기
n = int(input())
s = input()
print(n * s)

# 6038 : [기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
print(int(a) ** int(b))

# 6039 : [기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기
a, b = input().split()
print(float(a) ** float(b))
