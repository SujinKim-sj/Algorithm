n = int(input())
is_prime = [True] * 4000010
arr = [0] * 4000010

# 1) n개의 소수 배열 구하기
i = 2
while i * i <= 4000000:
    if is_prime[i]:
        for j in range(i + i, 4000001, i):
            is_prime[j] = False
    i += 1

idx = 0
for i in range(2, 4000000):
    if is_prime[i]:
        arr[idx] = i
        idx += 1

# 2) 연속된 소수의 합과 n 비교
sum = arr[0]
s, e = 0, 0
cnt = 0

while e < idx:
    if sum == n:
        cnt += 1
        e += 1
        sum += arr[e]
    elif sum < n:
        e += 1
        sum += arr[e]
    else:
        sum -= arr[s]
        s += 1

print(cnt)