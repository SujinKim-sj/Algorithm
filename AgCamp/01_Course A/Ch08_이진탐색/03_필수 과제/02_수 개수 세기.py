def getStartPoint(value):
    # start는 항상 value보다 작은 값을 가리킨다
    # end는 항상 value보다 큰 값을 가리킨다

    if n_arr[0] < value:
        start = 0
    else:
        if n_arr[0] > value:
            return -1  # 수가 없으므로 -1 반환
        else:
            return 0  # 첫 번째 반환

    if n_arr[n - 1] >= value:
        end = n - 1
    else:
        return -1

    while start + 1 < end:  # start와 end가 붙어있지 않다면
        mid = (start + end) // 2

        if n_arr[mid] < value:
            start = mid
        else:
            end = mid

    if n_arr[end] == value:
        return end
    else:
        return -1  # 값이 존재하지 않으므로


def getEndPoint(value):
    # start는 value보다 항상 작거나 같은 값을 가리킨다
    # end는 value보다 항상 큰 값을 가리킨다

    if n_arr[0] <= value:
        start = 0
    else:
        return -1

    if n_arr[n - 1] > value:
        end = n - 1
    else:
        if n_arr[n - 1] < value:
            return -1  # 값이 없음
        else:
            return n - 1

    while start + 1 < end:
        mid = (start + end) // 2

        if n_arr[mid] <= value:
            start = mid
        else:
            end = mid

    if n_arr[start] == value:
        return start
    else:
        return -1


n, q = map(int, input().split())
n_arr = list(map(int, input().split()))
q_arr = list(map(int, input().split()))

n_arr.sort()

# 숫자의 개수 출력
for i in range(q):
    x = q_arr[i]

    front, rear = getStartPoint(x), getEndPoint(x)

    if front == -1:
        print(0)
    else:
        print(rear - front + 1)