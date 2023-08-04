n = int(input())
arr = list(map(int, input().split()))
arr.sort()

s, e = 0, n - 1
ans1 = arr[0]
ans2 = arr[n - 1]

while s < e:
    if abs(arr[s] + arr[e]) < abs(ans1 + ans2):
        ans1 = arr[s]
        ans2 = arr[e]

    if arr[s] + arr[e] < 0:
        s += 1
    else:
        e -= 1

print(ans1, ans2)