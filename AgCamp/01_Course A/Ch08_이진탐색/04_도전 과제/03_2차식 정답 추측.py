a = int(input())

s, e = 1, 1000000000000000000
answer = 0
while s <= e:
    mid = (s + e) // 2

    if a == mid * mid + mid:
        answer = mid
        break
    elif a < mid * mid + mid:
        e = mid - 1
    else:
        s = mid + 1
        answer = mid

print(answer)