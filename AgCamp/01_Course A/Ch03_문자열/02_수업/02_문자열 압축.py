s = input()
s += "#"
cnt = 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if cnt != 1:
            print(cnt, end="")
        print(s[i - 1], end="")
        cnt = 1
    else:
        cnt += 1
