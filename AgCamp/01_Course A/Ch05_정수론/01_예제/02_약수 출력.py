n = int(input())
arr = []
i = 1
cnt = 0

while i * i <= n:
    if n % i == 0:
        print(i, end=" ")
        if n / i != i:
            arr.append(n // i)
            cnt += 1
    i += 1

for i in range(cnt - 1, -1, -1):
    print(arr[i], end=" ")
