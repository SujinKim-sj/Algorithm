k = int(input())
x = k
i = 2
cnt = 0
arr = [0] * 50

while i * i <= k:
    while x % i == 0:
        arr[cnt] = i
        x //= i
        cnt += 1
    i += 1

if x != 1:
    arr[cnt] = x
    cnt += 1  # cnt가 증가하여 음식의 개수도 증가한다

print(cnt)
for i in range(cnt):
    print(arr[i], end=" ")