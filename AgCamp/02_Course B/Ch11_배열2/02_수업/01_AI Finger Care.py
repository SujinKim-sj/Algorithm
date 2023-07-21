n = input()
keyboard = ["1qaz", "2wsx", "3edc", "4rfv5tgb", "6yhn7ujm", "8ik,", "9ol.", "0p;/-['=]"]

for i in keyboard:
    cnt = 0
    for j in range(len(n)):
        if n[j] in i:
            cnt += 1

    print(cnt, end=" ")