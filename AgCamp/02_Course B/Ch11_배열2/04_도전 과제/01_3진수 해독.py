password = ["CEFGHIJKLMNSTUVWXYZ", "ADOPQR", "B"]

test = int(input())
for t in range(test):
    print("#" + str(t + 1), end=" ")

    s1, s2 = map(str, input().split())
    x, y = "", ""  # 해독한 암호 3진수 담을 문자열

    for i in range(len(s1)):
        for j in range(len(password)):
            if s1[i] in password[j]:
                x += str(j)
            if s2[i] in password[j]:
                y += str(j)

    if x == y:
        print(1)
    else:
        print(0)