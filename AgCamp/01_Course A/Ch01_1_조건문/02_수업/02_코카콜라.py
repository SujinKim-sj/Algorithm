n = int(input())
answer = 0

if n % 8 == 0:
    answer = 2
elif n % 8 == 6:
    answer = 4
elif n % 8 == 7:
    answer = 3
else:
    answer = n % 8

print(answer)