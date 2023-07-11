t = int(input())

arr = []
for i in range(100):
    for j in range(1, i + 1):
        arr.append(i)

for i in range(t):
    s, e = map(int, input().split())
    sum = 0

    for j in range(s, e + 1):
        sum += arr[j - 1]

    print("#" + str(i + 1), sum)