n = int(input())
answer = 0
max_answer = 0

for i in range(n):
    a, b, c = map(int, input().split())

    if a == b == c:
        answer = 10000 + a * 1000
    elif a == b and a != c:
        answer = 1000 + a * 100
    elif b == c and a != b:
        answer = 1000 + b * 100
    elif a == c and b != c:
        answer = 1000 + c * 100
    else:
        answer = max(a, b, c) * 100

    max_answer = max(max_answer, answer)

print(max_answer)