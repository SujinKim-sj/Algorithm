test = int(input())

for t in range(test):
    print("#" + str(t + 1), end=" ")
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = 0
    graph = [0 for i in range(210)]

    for i in range(n):
        graph[i] = arr[tmp]
        tmp = arr[tmp]

    for i in range(len(graph)):
        if graph[i] == x:
            print(i + 1)
            break

    if x not in graph:
        print(-1)