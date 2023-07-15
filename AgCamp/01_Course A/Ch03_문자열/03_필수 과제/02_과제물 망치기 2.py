t = int(input())
arr = ['A', 'E', 'I', 'O', 'U']

for i in range(t):
    print('#', end='')
    print(i + 1, end=' ')

    s = input()
    new_s = ""
    for j in range(len(s)):
        if s[j] not in arr:
            new_s += s[j]

    print(new_s)