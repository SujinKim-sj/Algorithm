# 파이썬 기초 100제
# 기초-비트단위논리연산
# 비트단위(bitwise) 연산자
# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)



# 6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)   # ~ : tilde, 틸드

# 6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
a, b = input().split()
print(int(a) & int(b))

# 6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
a, b = input().split()
print(int(a) | int(b))

# 6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
a, b = input().split()
print(int(a) ^ int(b))
