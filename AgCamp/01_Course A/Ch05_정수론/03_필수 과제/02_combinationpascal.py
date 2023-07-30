n, m = map(int, input().split())

if n == 0 or m == 0 or n == m:
    print(1)
else:
    answer = 1
    for i in range(1, m + 1):
        answer *= n - i + 1
        answer //= i

    print(answer)