def sort_arr(arr):
    # 1. 개수가 많은 i
    for i in range(n):
        for j in range(n - i - 1):
            if vector[arr[j]][0] < vector[arr[j + 1]][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif vector[arr[j]][0] == vector[arr[j + 1]][0]:
                # 2. 같으면 위치가 빠른 물건 먼저
                if vector[arr[j]][1] > vector[arr[j + 1]][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test = int(input())

for t in range(test):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0] * 1000
    vector = [(0, 0, 0)] * 1000

    for i in range(n):
        cnt[arr[i]] += 1  # 물건 개수 세기

    for i in range(n):
        vector[arr[i]] = (cnt[arr[i]], arr.index(arr[i]), arr[i])

    sort_arr(arr)  # vector 사용해서 정렬

    print("#" + str(t + 1))

    for i in range(n):
        print(arr[i], end=" ")
    print("")