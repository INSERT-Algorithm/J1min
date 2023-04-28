resultList = [input().split() for _ in range(8)]
resultList.sort(key=lambda x: x[0])
scoreList = [10, 8, 6, 5, 4, 3, 2, 1]
r, b = 0, 0

for idx, (_, team) in enumerate(resultList):
    if team == 'R':
        r += scoreList[idx]
    else:
        b += scoreList[idx]

print('Red' if r > b else 'Blue')
