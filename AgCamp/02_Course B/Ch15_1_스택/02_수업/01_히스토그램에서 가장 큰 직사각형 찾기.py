n = int(input())
arr = [0 for i in range(100010)]
arr2 = list(map(int, input().split()))

l = [0 for i in range(100010)]
r = [0 for i in range(100010)]
stack = []

for i in range(1, n + 1):
    arr[i] = arr2[i - 1]

arr[0] = -1
stack.append(0)

for i in range(1, n + 1):
    while arr[stack[-1]] >= arr[i]:
        stack.pop()
    l[i] = stack[-1]
    stack.append(i)

while len(stack) != 0:
    stack.pop()

arr[n + 1] = -1
stack.append(n + 1)

for i in range(n, 0, -1):
    while arr[stack[-1]] >= arr[i]:
        stack.pop()
    r[i] = stack[-1]
    stack.append(i)

answer = 0
for i in range(1, n + 1):
    area = arr[i] * (r[i] - l[i] - 1)
    if answer < area:
        answer = area

print(answer)