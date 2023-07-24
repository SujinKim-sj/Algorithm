s = input()
reverse = ""

for i in range(len(s) - 1, -1, -1):
  reverse += s[i]

print(reverse)