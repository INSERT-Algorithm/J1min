def gap(a, b):
    return abs(a - b)


T = int(input())

for _ in range(T):
    n = int(input())
    start = input()
    end = input()

    answer = 0

    bw = 0  # b여야 하는데 w인 경우
    wb = 0  # w여야 하는데 b인 경우

    for i in range(n):
        if start[i] != end[i]:  # 각자 다른 경우를 카운팅
            if start[i] == 'W':
                bw += 1
            else:
                wb += 1

    a = bw + wb
    b = gap(bw, wb)

    step1 = gap(a, b) // 2  # step 1. 서로 뒤바꾼 경우 카운트
    step2 = 0

    for i in range(n):
        if start[i] != end[i]:
            step2 += 1  # step2. 그냥 뒤집은 경우 카운트

    step2 -= (answer * 2)  # 서로 다른 경우 - (뒤바꾼 경우 * 2) => 그냥 뒤집은 경우

    print(step1 + step2)
