t = int(input())
name = ["A", "N", "D", "R", "E", "W"]

for i in range(t):
    print('#', end='')
    print(i + 1, end=' ')

    s = input()
    for j in range(len(s)):
        if s[j] not in name:
            print(s[j], end='')
    print('')
