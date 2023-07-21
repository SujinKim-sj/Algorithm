m, d = map(int, input().split())

# 목요일 (1월 1일)부터 시작
arr = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = d
for i in range(m - 1):
  week += month[i]

week %= 7
print(arr[week - 1])