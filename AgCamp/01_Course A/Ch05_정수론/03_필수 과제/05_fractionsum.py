a, b = map(int, input().split())
c, d = map(int, input().split())

bunmo = b * d
bunja = a * d + b * c

a = bunmo
b = bunja

while b % a != 0:
  r = b % a
  b = a
  a = r

print(bunja // a, bunmo // a)