n = int(input())
student = [list(map(int, input().split())) for i in range(n)]
arr = [0] * n

for i in range(n):
  cnt = 0
  for j in range(n):
    if i == j:
      continue
    if student[i][0] == student[j][0] or student[i][1] == student[j][1] or student[i][2] == student[j][2] or student[i][3] == student[j][3] or student[i][4] == student[j][4]:
        arr[i] += 1

max_arr = arr[0]
president = 0

for i in range(n):
  if max_arr < arr[i]:
    max_arr = arr[i]
  elif max_arr == arr[i]:
    continue

president = arr.index(max_arr) + 1
print(president)