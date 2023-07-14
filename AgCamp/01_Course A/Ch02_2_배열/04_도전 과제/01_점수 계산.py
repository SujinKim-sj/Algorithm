n = int(input())
arr = list(map(int, input().split()))

cnt = 0
score = []
for i in range(n):
    if arr[i] == 1:
        cnt += 1
        score.append(cnt)
    else:
        cnt = 0

sum = 0
for i in range(len(score)):
    sum += score[i]

print(sum)