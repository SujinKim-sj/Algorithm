n = int(input())
is_prime = [True] * (n + 1)

i = 2
while i * i <= n:
    if is_prime[i] == True:
        for j in range(i + i, n + 1, i):
            is_prime[j] = False
    i += 1

for i in range(2, n + 1):
    if is_prime[i] == True:
        print(i, end=' ')