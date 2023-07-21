arr = list(map(int, input().split()))
card = [1, 1, 2, 2, 2, 8]

for i in range(len(card)):
  print(card[i] - arr[i], end=" ")