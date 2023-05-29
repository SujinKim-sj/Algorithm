# DFS 실전문제 3 - 음료수 얼려먹기

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 종료조건 1 : 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    # 성공조건
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1

        # 상하좌우 위치 재귀호출
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        return True

    # 종료조건 2
    return False

# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            print(dfs(i, j))
            result += 1

print(result)