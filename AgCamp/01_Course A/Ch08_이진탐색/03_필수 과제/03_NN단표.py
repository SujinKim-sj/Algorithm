def getOrder(x):
    result = 0
    for i in range(1, n + 1):
        if i * n < x:
            result += n
        else:
            if x % i == 0:
                result += (x // i) - 1
            else:
                result += x // i

    return result + 1


n = int(input())
k = int(input())

s, e = 1, n * n + 1  # e는 mid값에 포함할 수 없으므로 + 1

while s + 1 < e:
    # s : 항상 정답이 되는 숫자보다 작거나 같은 숫자
    # e : 항상 정답이 되는 숫자보다 큰 숫자
    mid = (s + e) // 2
    myOrder = getOrder(mid)  # mid가 몇 번째 숫자인지 구하기

    if myOrder <= k:  # <=를 함으로써 s는 항상 존재하는 숫자만 나오게 된다
        s = mid  # mid보다 작은 숫자는 버림
    else:
        e = mid

print(s)