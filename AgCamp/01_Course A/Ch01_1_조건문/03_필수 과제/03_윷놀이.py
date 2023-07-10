sum = 0

for i in range(3):
    a, b, c, d = map(int, input().split())
    sum = a + b + c + d

    if sum == 0:  # 윷
        print("D")
    elif sum == 1:  # 걸
        print("C")
    elif sum == 2:  # 개
        print("B")
    elif sum == 3:  # 도
        print("A")
    else:  # 모
        print("E")
