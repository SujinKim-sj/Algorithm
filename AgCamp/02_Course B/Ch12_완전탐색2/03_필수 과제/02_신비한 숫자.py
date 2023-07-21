def prime(a):
    cnt = 0
    i = 2

    while i * i <= a:
        if a % i == 0:
            cnt += 1
        i += 1

    if a != 1 and cnt == 0:
        return True
    return False


q = int(input())

for i in range(q):
    a = int(input())
    answer = False

    # 1번
    for j in range(1, a):
        if prime(j) and prime(a - j):
            answer = True

    # 2번
    # for j in range(1, a + 1):
    #     if not prime(j):
    #         continue
    #
    #     for k in range(j + 1, a + 1):
    #         if not prime(k):
    #             continue
    #         if j + k == a:
    #             answer = True

    if answer:
        print("Yes")
    else:
        print("No")