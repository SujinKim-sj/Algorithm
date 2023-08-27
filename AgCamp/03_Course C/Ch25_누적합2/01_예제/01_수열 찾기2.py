n = int(input())
arr = [0 for i in range(100010)]
arr2 = list(map(int, input().split()))
delta = [0 for i in range(100010)]
prefix = [0 for i in range(100010)]

first = True

for i in range(1, n + 1):
    arr[i] = arr2[i - 1]

q = int(input())
for _ in range(q):
    action = list(map(int, input().split()))
    a = action[0]

    if a == 1:
        b, c, d = action[1], action[2], action[3]
        delta[b] += d
        delta[c + 1] -= d
    else:
        b = action[1]
        if first:
            for i in range(1, n + 1):
                prefix[i] = prefix[i - 1] + delta[i]

            first = False

        print(prefix[b] + arr[b])