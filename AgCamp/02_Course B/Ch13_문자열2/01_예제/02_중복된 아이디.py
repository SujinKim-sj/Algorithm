n = int(input())
s = input()
visited = {}

for i in range(1, n + 1):
    flag = True
    for j in range(n - i + 1):
        p = ""
        for k in range(i):
            p += s[j + k]

        if visited.get(p):
            flag = False
        visited[p] = True;

    if flag:
        print(i)
        break