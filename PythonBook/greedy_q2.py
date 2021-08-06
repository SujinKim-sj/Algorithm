# 그리디 실전문제 2 - 숫자 카드게임

n, m = map(int, input().split())    # n = 행, m = 열
result = 0

# 2중 반복문 구조 이용
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)