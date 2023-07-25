alpha = input()
result = [0 for i in range(60)]  # push, pop 출력 담을 배열
result_len = 0
stack = ['' for i in range(30)]
top = 0
cursor = 0
cur_alpha = 'a'
flag = False  # 가능, 불가능 판단

while True:
    t = ''  # 스택의 맨 위의 값
    if top == 0:
        t = 0
    else:
        t = stack[top - 1]

    current = alpha[cursor]  # 지금 뽑아야할 값
    if t == current:
        stack[top - 1] = 0
        top -= 1
        result[result_len] = 0  # pop
        result_len += 1
        cursor += 1

        if cursor >= len(alpha):
            flag = True  # 성공
            break
    else:
        if cur_alpha >= chr(ord('a') + len(alpha)):
            flag = False
            break

        stack[top] = cur_alpha
        top += 1
        result[result_len] = 1  # push
        result_len += 1
        cur_alpha = chr(ord(cur_alpha) + 1)

if flag:
    for i in range(result_len):
        if result[i] == 0:
            print("pop")
        else:
            print("push")
else:
    print("impossible")