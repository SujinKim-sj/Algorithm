def check(x):
    sum = 0
    for i in range(n):
        if x < arr[i][0]:
            continue
        elif x <= arr[i][1]:
            sum += x - arr[i][0] + 1
        else:
            sum += arr[i][1] - arr[i][0] + 1

    return sum >= idx


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

idx = int(input())
idx += 1
answer = 0
s, e = 0, 1000000000

while s <= e:
    mid = (s + e) // 2

    if check(mid):
        answer = mid
        e = mid - 1
    else:
        s = mid + 1

print(answer)