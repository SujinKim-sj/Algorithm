a, b, c = map(int, input().split())

max = a

if max < b:
    max = b
    if max < c:
        max = c
elif max < c:
    max = c
    if max < b:
        max = b

print(max)