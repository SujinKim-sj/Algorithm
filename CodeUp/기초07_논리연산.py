# 파이썬 기초 100제
# 기초 - 논리연산

# 6052 : [기초-논리연산] 정수 입력받아 참 거짓 평가하기
a = int(input())
print(bool(a))    # bool() : 0이면 False, 이외에는 True 출력

# 6053 : [기초-논리연산] 참 거짓 바꾸기
a = bool(int(input()))
print(not a)
# 어떤 불 값이나 변수에 not True, not False, not a 와 같은 계산이 가능

# 6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기
a, b = input().split()
a = int(a)
b = int(b)

print(bool(a) and bool(b))

# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print((c and (not d)) or ((not c) and d))

# 6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print((not c and not d) or (c and d))
# 풀이2) print(c == d)

# 6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기
a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print(not (c or d))
# 풀이2) print(c == False and d == False)
