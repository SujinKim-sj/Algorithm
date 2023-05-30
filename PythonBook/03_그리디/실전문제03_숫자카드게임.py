n, m = map(int, input().split())

answer = 0

# 답안 1)
for i in range(n):
    data = list(map(int, input().split()))

    # 현재 줄에서 가장 작은 수 찾기
    min_card = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    answer = max(answer, min_card)

# 답안 2)
for i in range(n):
    data = list(map(int, input().split()))
    min_card = 10001
    for a in data:
        min_card = min(min_card, a)
    answer = max(answer, min_card)

print(answer)