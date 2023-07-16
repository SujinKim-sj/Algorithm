n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(k):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr[n - k])