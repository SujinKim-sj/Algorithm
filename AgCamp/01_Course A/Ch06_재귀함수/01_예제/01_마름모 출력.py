def recur(line):
    if line == n + 1:
        return

    for i in range(n - line):
        print(' ', end="")

    for i in range(2 * line - 1):
        print('*', end="")

    print("")

    recur(line + 1)

    if line == n:
        return

    for i in range(n - line):
        print(' ', end="")

    for i in range(2 * line - 1):
        print('*', end="")

    print("")


n = int(input())
recur(1)