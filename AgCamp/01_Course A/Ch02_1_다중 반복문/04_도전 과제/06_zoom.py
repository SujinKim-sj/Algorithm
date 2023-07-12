k = int(input())
# 주의 : X는 대문자로 출력
for i in range(1, 3 * k + 1):
    for j in range(k):
        if i <= k:
            print("", end="")
        if k + 1 <= i <= 2 * k:
            print(" ", end="")
        if 2 * k + 1 <= i <= 3 * k:
            print("X", end="")

    for j in range(k):
        if i <= k:
            print("**", end="")
        if k + 1 <= i <= 2 * k:
            print("X", end="")
        if 2 * k + 1 <= i <= 3 * k:
            print(" ", end="")

    for j in range(k):
        if i <= k:
            print("X", end="")
        if k + 1 <= i <= 2 * k:
            print("*", end="")
        if 2 * k + 1 <= i <= 3 * k:
            print("*", end="")
    print("")


# ######
# 1
# for i in range(k):
#     for j in range(k):
#         print("**", end="")
#
#     for j in range(k):
#         print("x", end="")
#     print("")
#
# # 2
# for i in range(k):
#     for j in range(k):
#         print(" ", end="")
#
#     for j in range(k):
#         print("x", end="")
#
#     for j in range(k):
#         print("*", end="")
#     print("")
#
# # 3
# for i in range(k):
#     for j in range(k):
#         print("x", end="")
#
#     for j in range(k):
#         print(" ", end="")
#
#     for j in range(k):
#         print("*", end="")
#     print("")

# 일단 행을 기준으로
# 1~k 행
# k+1~2k 행
# 2k+1~3k 행을 구현하려 해보세요
# 3중 혹은 4중반복문으로 구현이 되어도 좋으니 규칙을 찾아 나누어 구현해보시는게 중요