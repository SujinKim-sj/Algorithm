s = input()
d = ord('a') - ord('A')

for i in range(len(s)):
    if 'a' <= s[i] and s[i] <= 'z':
        print(chr(ord(s[i]) - d), end="")
    elif 'A' <= s[i] and s[i] <= 'Z':
        print(chr(ord(s[i]) + d), end="")
    else:
        print(s[i], end="")
