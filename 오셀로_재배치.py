from collections import Counter
import math


def gap(a, b):
    return abs(a - b)


n = int(input())

for _ in range(n):
    k = int(input())
    s = list(input())  # 초기
    e = list(input())  # 목표
    count = 0

    swc = 0  # b여야 하는데 w인 경우
    sbc = 0  # w여야 하는데 b인 경우

    for i in range(k):
        if s[i] != e[i]:
            if s[i] == 'W':
                swc += 1
            else:
                sbc += 1

    a = swc + sbc
    b = gap(swc, sbc)

    count = gap(a, b) // 2  # step 1. 서로 뒤바꾼 경우

    count2 = 0
    for i in range(k):
        if s[i] != e[i]:
            count2 += 1  # step2. 그냥 뒤집은 경우

    count2 -= (count * 2)  # 뒤집은 경우 카운트 해주고 뒤바꾼 경우만큼 빼줘서 진짜 뒤집은 경우 카운팅

    print(count + count2)
