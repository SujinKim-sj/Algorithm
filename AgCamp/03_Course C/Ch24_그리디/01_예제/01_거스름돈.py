n = int(input())
arr = [500, 100, 50, 5, 1]
answer = 0

for i in range(5):
    answer += n // arr[i]
    n %= arr[i]

print(answer)