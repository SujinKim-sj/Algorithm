n = int(input())
arr = [[0 for i in range(4)] for i in range(110)]
cnt = [0 for i in range(110)]

for i in range(1, n + 1):
    arr[i] = list(map(int, input().split()))

for i in range(110):
    for j in range(110):
        idx = 0
        # 색종이 최종번호 알아내기
        for k in range(1, n + 1):
            if arr[k][0] <= i and i < arr[k][0] + arr[k][2] and arr[k][1] <= j and j < arr[k][1] + arr[k][3]:
                idx = k

        cnt[idx] += 1

for i in range(1, n + 1):
    print(cnt[i])