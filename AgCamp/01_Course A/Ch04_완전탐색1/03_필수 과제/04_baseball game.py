n = int(input())
result = 0  # 답의 총 개수
arr = []
for i in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and i != k:
                flag = False

                for p in range(n):
                    # ijk가 조건을 만족하는지 체크
                    first = arr[p][0] // 100
                    second = arr[p][0] // 10 % 10
                    third = arr[p][0] % 10

                    strike, ball = 0, 0
                    if first == i: strike += 1
                    if second == j: strike += 1
                    if third == k: strike += 1

                    if i == second or i == third: ball += 1
                    if j == first or j == third: ball += 1
                    if k == first or k == second: ball += 1

                    if arr[p][1] != strike or arr[p][2] != ball:
                        flag = True  # 한 번이라도 조건에 만족하지 않으면

                if not flag:
                    result += 1

print(result)