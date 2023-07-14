arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

max = arr[0]
index = 0

for i in range(9):
    if max <= arr[i]:
        max = arr[i]
        index = i + 1

print(max)
print(index)