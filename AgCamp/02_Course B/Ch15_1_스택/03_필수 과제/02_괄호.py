ps = input()
stack = []
flag = True

for i in range(len(ps)):
  if ps[i] == '(':
    stack.append(ps[i])
  else:
    if len(stack) == 0:
      flag = False
      break
    stack.pop()

if not flag or len(stack) > 0:
  print("NO")
else:
  print("YES")