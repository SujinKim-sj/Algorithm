def num_print(cur):
    if cur == n:
        for j in range(n):
            print(arr[j], end='')
        print('')
        return

    for i in range(m):
        if visited[i]:
            continue
        arr[cur] = i
        visited[i] = True

        num_print(cur + 1)
        visited[i] = False


# n자리 m진수
n, m = map(int, input().split())
arr = [0] * 50
visited = [False] * 50  # 방문여부 배열 추가

num_print(0)