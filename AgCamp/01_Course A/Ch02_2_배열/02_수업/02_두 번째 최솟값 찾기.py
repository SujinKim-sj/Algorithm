arr = []

for i in range(9):
    n = int(input())
    arr.append(n)

min = arr[0]
index = 0

for i in range(9):
    if min >= arr[i]:
        min = arr[i]
        index = i

arr[index] = -1

# 두 번째 최솟값 찾기
second_min = 10000000
for i in range(9):
    if arr[i] == -1:
        continue
    else:
        if second_min >= arr[i]:
            second_min = arr[i]
            index = i + 1

print(second_min)
print(index)