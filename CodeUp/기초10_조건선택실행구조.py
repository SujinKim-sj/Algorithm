# 파이썬 기초 100제
# 기초 - 조건/선택 실행구조

# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a, b, c = input().split()

if int(a) % 2 == 0:
    print(a)
if int(b) % 2 == 0:
    print(b)
if int(c) % 2 == 0:
    print(c)

# 6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2 == 0:
    print("even")
else:
    print("odd")
    
# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
a = int(input())

if a < 0 and a % 2 == 0:
    print("A")
elif a < 0 and a % 2 != 0:
    print("B")
elif a > 0 and a % 2 == 0:
    print("C")
elif a > 0 and a % 2 != 0:
    print("D")
    
# 6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
score = int(input())

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")
    
# 6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기
grade = input()

if grade == 'A':
    print("best!!!")
elif grade == 'B':
    print("good!!")
elif grade == 'C':
    print("run!")
elif grade == 'D':
    print("slowly~")
else:
    print("what?")
    
# 6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
mon = int(input())

if mon // 3 == 1:
    print("spring")
elif mon // 3 == 2:
    print("summer")
elif mon // 3 == 3:
    print("fall")
else:
    print("winter")
