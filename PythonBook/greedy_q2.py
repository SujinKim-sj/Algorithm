# 그리디 실전문제 2 - 숫자 카드게임

n, m = map(int, input().split())    # n = 행, m = 열
result = 0

# min() 함수 이용
""" 
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)   # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기

"""
# 2중 반복문 구조 이용
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)