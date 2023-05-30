n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
arr.sort()
first_max = arr[n - 1]
second_max = arr[n - 2]

# 답안1
# while True:
#     # 가장 큰 수를 K번 더하기
#     for i in range(k):
#         if m == 0:
#             break
#         answer += first_max
#         m -= 1  # 더할 때마다 1씩 빼기
#     if m == 0:
#         break
#     # 두 번째로 큰 수를 한 번 더하기
#     answer += second_max
#     m -= 1


# 답안2
count = int(m / (k + 1)) * k
count += m % (k + 1)

answer += (count) * first_max  # 가장 큰 수 더하기
answer += (m - count) * second_max  # 두번째로 큰 수 더하기


print(answer)