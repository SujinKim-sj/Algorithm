a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_win = 0
b_win = 0

for i in range(10):
    if a[i] > b[i]:
        a_win += 1
    elif a[i] < b[i]:
        b_win += 1
    else:
        continue

if a_win > b_win:
    print("A")
elif a_win < b_win:
    print("B")
else:
    print("D")
