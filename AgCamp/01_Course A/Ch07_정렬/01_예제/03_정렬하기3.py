# 계수 정렬

n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 1010

for i in range(n):
  cnt[arr[i]] += 1

for i in range(1010):
  for j in range(cnt[i]): # cnt[i] == 1이면 1번 출력
    print(i, end=" ")