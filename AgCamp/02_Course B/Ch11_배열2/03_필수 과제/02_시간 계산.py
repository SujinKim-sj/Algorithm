test = int(input())

for t in range(test):
    print("#" + str(t + 1), end=" ")
    h, m, x, y = map(int, input().split())
    h += x
    m += y

    h += m // 60
    m %= 60

    h %= 12
    if h == 0:
        h = 12

    print(h, m)