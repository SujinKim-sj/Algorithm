test = int(input())

for t in range(test):
    s = input()
    answer = 0

    for i in range(26):
        if s[0] == chr(ord('a') + i):
            answer = i * 25

            for j in range(26):
                answer += 1
                if s[0] == chr(ord('a') + j):
                    answer -= 1
                if s[1] == chr(ord('a') + j):
                    break

    print("#" + str(t + 1), answer)

