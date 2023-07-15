t = int(input())  # 테스트 케이스 수

for i in range(t):
    print("#", end="")
    print(i + 1, end=" ")

    s = input()
    idx = 0

    while idx < len(s):
        if s[idx] >= '0' and s[idx] <= '9':
            for i in range(int(s[idx])):
                print(s[idx + 1], end="")
            idx += 2
        else:
            print(s[idx], end="")
            idx += 1
    print("")