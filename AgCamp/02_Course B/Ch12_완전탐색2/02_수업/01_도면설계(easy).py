n = int(input())
arr = [[0 for i in range(2)] for i in range(1010)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

answer = 0
for i in range(1, 1010):
    l = 1010
    r = -1
    for j in range(n):
        if arr[j][1] >= i:  # 높이가 i보다 크거나 같으면 왼, 오를 찾기
            if l > arr[j][0]:
                l = arr[j][0]
            if r < arr[j][0]:
                r = arr[j][0]

    if r != -1:
        answer += r - l + 1

print(answer)