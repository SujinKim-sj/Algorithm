# 내가 푼 풀이

# 현재 나이트의 위치 입력받기
start = input()
x = ord(start[0])   # 열 (문자를 아스키코드로 변환)
y = start[1]        # 행

# 나이트가 이동할 수 있는 8가지 방향 정의
move_type = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
for i in range(8):
    nx = chr(x + move_type[i][0])
    ny = int(y) + move_type[i][1]

    # 해당 위치로 이동이 가능하다면 카운트 증가하고 아니면 무시하고 다음 경우의 수 진행
    if nx < 'a' or nx > 'h' or ny < 1 or ny > 8:
        continue
    else:
        count += 1

print(count)