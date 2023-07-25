from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()

arr.sort()  # 정렬
queue.append(arr[0])

for i in range(1, n):
    if arr[i] > queue[0] + k:
        queue.popleft()

    queue.append(arr[i])

print(len(queue))