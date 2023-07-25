n = int(input())
arr2 = list(map(int, input().split()))
arr = [0 for i in range(500010)]
st = []

for i in range(1, n + 1):
  arr[i] = arr2[i - 1]

arr[0] = 2000000000
st.append(0)

for i in range(1, n + 1):
  while arr[st[-1]] < arr[i]:
    st.pop()
  print(st[-1], end=" ")
  st.append(i)