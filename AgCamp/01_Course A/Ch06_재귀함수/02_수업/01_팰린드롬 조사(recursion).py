def recur(start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False

    return recur(start + 1, end - 1)


s = input()
if recur(0, len(s) - 1) == True:
    print("YES")
else:
    print("NO")
