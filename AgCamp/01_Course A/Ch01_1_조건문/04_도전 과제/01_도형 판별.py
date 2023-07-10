a = int(input())
b = int(input())
c = int(input())

sum = a + b + c
answer = ""

if a == b == c == 60:
    answer = "Equilateral"
elif sum == 180 and a == b or sum == 180 and a == c or sum == 180 and b == c:
    answer = "Isosceles"
elif sum == 180 and a != b or sum == 180 and a != c or sum == 180 and b != c:
    answer = "Scalene"
elif sum != 180:
    answer = "Error"

print(answer)