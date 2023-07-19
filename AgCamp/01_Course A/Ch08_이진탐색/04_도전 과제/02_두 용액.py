n = int(input())
arr = list(map(int, input().split()))
minus = []
plus = []
# 0에 가까운 용액을 만들어내는 두 용액
# 1) 음수, 양수 배열 분리
for i in range(n):
    if arr[i] > 0:
        plus.append(arr[i])
    else:
        minus.append(arr[i])

plus.sort()
answer = 1000000000
nArr = []
for i in range(len(minus)):
    x = abs(minus[i])
    tmp = -1
    s, e = 0, len(plus) - 1

    while s <= e:
        mid = (s + e) // 2

        if plus[mid] <= x:
            tmp = plus[mid]
            s = mid + 1
        else:
            e = mid - 1

    answer = min(answer, abs(x - tmp))
    nArr.append((minus[i], tmp))

print(nArr)
if len(nArr) == 1:
    print(nArr[0][0], nArr[0][1])
else:
    min_nArr = nArr[0][0]
    for i in range(len(nArr)):
        if min_nArr > nArr[i][0]:
            print(nArr[i][0], nArr[i][1])
            break
