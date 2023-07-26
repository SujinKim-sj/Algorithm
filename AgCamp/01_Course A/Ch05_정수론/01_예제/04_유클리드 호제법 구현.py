a, b = map(int, input().split())
answer = 0

while b % a != 0:
  r = b % a
  b = a
  a = r

# print("최대공약수는", str(a), "입니다.") # 한글 출력 오류남
print(a)