arr = [list(map(int, input().split())) for _ in range(9)]

max_n = arr[0][0]
idx_i, idx_j = 0, 0

for i in range(9):
    for j in range(9):
        if max_n < arr[i][j]:
            max_n = arr[i][j]
            idx_i = i
            idx_j = j
        elif max_n == arr[i][j]:
            max_n = arr[i][j]
            if idx_i > i:
                idx_i = i
                idx_j = j
            elif idx_i == i:
                if idx_j > j:
                    idx_i = i
                    idx_j = j

print(max_n)
print(idx_i + 1, idx_j + 1)