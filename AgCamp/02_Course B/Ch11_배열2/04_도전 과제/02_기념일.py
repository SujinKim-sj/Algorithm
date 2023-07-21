test = int(input())
calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(test):
  print("#" + str(t + 1), end=" ")
  answer = 1
  m, d, cur_m, cur_d = map(int, input().split())
  for i in range(m, cur_m):
    answer += calendar[i]

  answer += cur_d - d
  print(answer)