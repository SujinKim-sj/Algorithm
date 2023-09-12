test = int(input())

for t in range(1, test + 1):
    answer = 1e9
    flowers = list(map(int, input().split()))
    flen = len(flowers)

    for i in range(flen):
        for j in range(i + 1, flen):
            for k in range(j + 1, flen):
                a, b, c = flowers[i], flowers[j], flowers[k]
                lcm = a * b

                while b % a != 0:
                    r = b % a
                    b = a
                    a = r

                gcd = a
                lcm //= gcd

                lcm2 = c * lcm

                while lcm % c != 0:
                    r = lcm % c
                    lcm = c
                    c = r

                lcm2 //= c
                answer = min(answer, lcm2)

    print("#", end="")
    print(t, answer)