# 파이썬 기초 100제
# 기초 - 입출력

# 6009 : [기초-입출력] 문자 1개 입력받아 그대로 출력하기
c = input()
print(c)

# 6010 : [기초-입출력] 정수 1개 입력받아 int로 변환하여 출력하기
num = int(input())
print(num)

# 6011 : [기초-입출력] 실수 1개 입력받아 변환하여 출력하기
f = float(input())
print(f)

# 6012 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기1
a = int(input())
b = int(input())

print(a)
print(b)

# 6013 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기1
c1 = input()
c2 = input()

print(c2)
print(c1)

# 6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)
f1 = float(input())

print(f1)
print(f1)
print(f1)

# 6015 : [기초-입출력] 정수 2개 입력받아 그대로 출력하기2
n1, n2 = input().split()

print(n1)
print(n2)

# 6016 : [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2
c1, c2 = input().split()
print(c2, c1)

# 6017 : [기초-입출력] 문장 1개 입력받아 3번 출력하기
s = input()
print(s, s, s)

# 6018 : [기초-입출력] 시간 입력받아 그대로 출력하기
h, m = input().split(':')
print(h, m, sep=':')

# 6019 : [기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 6020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
id1, id2 = input().split('-')
print(id1, id2, sep='')

# 6021 : [기초-입출력] 단어 1개 입력받아 나누어 출력하기
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')

# 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기
# 풀이1) - 내가 푼 풀이
time = input().split(':')
print(time[1])

# 풀이2)
h, m, s = input().split(':')
print(m)

# 6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기
word1, word2 = input().split()
print(word1 + word2)
