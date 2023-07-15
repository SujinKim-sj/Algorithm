t = int(input())

for i in range(t):
    n = int(input())

    # 테스트 케이스 번호 출력
    print("#" + str(i + 1))
    nsArr = []  # 문자열 속 숫자 담을 배열

    # 문자열 n번 입력받기
    for j in range(n):
        s = input()
        idx, idx2 = 0, 0
        ns = ""  # 연속된 숫자있으면 문자열에 담기

        while idx < len(s):
            while idx2 < len(s) and '0' <= s[idx2] <= '9':
                ns += str(s[idx2])
                if 'a' <= s[idx2] <= 'z':
                    ns += str(s[idx2])
                idx2 += 1

            idx2 += 1
            idx += 1

            if ns != "":
                nsArr.append(int(ns))
            ns = ""

    # 숫자 정렬 후 출력
    nsArr.sort()

    for j in range(len(nsArr)):
        print(nsArr[j], end=" ")
    print("")