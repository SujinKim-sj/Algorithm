def recur(cur, cnt, c, f):
  global answer
  if cur == n:
    if cnt != 0 and answer > abs(c - f):
      answer = abs(c - f) #최솟값
    return
  #print(1, cur, cnt, c, f)
  recur(cur + 1, cnt + 1, c + arr[cur][0], f * arr[cur][1])
  #print(2, cur, cnt, c, f)
  recur(cur + 1, cnt, c, f)


n = int(input())
arr = [[0 for i in range(2)] for i in range(20)]
answer = 1000000000

for i in range(n):
  arr[i] = list(map(int, input().split()))

#print(arr)
recur(0, 0, 0, 1)
print(answer)