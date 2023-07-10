a, b = map(int, input().split())
c = int(input())

answer = 0
if (a + b) // c >= 2:
    answer = (a + b) - (c * 2)
else:
    answer = a + b

print(answer)