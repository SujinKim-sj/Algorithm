n = int(input())  # 공간의 크기
plan = list(input().split())

x = 1
y = 1
move = ['L', 'R', 'U', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 이동 계획을 하나씩 확인
for i in plan:
    # 이동 후 좌표 구하기
    for j in range(4):
        if i == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)