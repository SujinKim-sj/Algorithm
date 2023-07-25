n = int(input())
h = list(map(int, input().split()))
stack = []
answer = 0

stack.append(0)

for i in range(1, n):
    while len(stack) != 0 and h[stack[-1]] < h[i]:
        answer += i - stack[-1] + 1
        stack.pop()

    if len(stack) != 0:
        answer += i - stack[-1] + 1
        if h[stack[-1]] == h[i]:
            stack.pop()

    stack.append(i)

print(answer)