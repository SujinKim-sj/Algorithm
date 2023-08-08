def dfs(cur, option):
    if cur == -1:  # 자식노드 존재x
        return
    if option == 0:
        print(cur, end=" ")
    dfs(arr[cur][0], option)

    if option == 1:
        print(cur, end=" ")
    dfs(arr[cur][1], option)

    if option == 2:
        print(cur, end=" ")


n = int(input())
arr = [[0, 0] for i in range(110)]

for i in range(n):
    a, b, c = map(int, input().split())
    arr[a][0] = b
    arr[a][1] = c

dfs(0, 0)  # 전위 순회
print("")
dfs(0, 1)  # 중위 순회
print("")
dfs(0, 2)  # 후위 순회
print("")
