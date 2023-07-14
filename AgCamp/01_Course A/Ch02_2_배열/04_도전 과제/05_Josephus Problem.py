n, k = map(int, input().split())
arr = [i + 1 for i in range(n)]
answer = []

idx = 0
count = 0

for i in range(n):
    idx += k - 1

    if idx >= len(arr):
        idx %= len(arr)

    answer.append(arr[idx])  # 2. K번째 값을 요세푸스 수열에 추가하는 작업
    arr.pop(idx)  # 3. 요세푸스 수열에 추가된 수는 배열에서 제외하는 작업

# n - 1번째 탈락자, n번째 탈락자 출력
print(answer[n - 2], answer[n - 1])