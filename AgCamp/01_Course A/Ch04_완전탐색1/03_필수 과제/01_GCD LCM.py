a, b = map(int, input().split())

lcm = a * b

while b % a != 0:
    r = b % a
    b = a
    a = r

gcd = a
lcm //= gcd

print(gcd)
print(lcm)