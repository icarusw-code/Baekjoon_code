# 일곱 난쟁이
from itertools import combinations
array = []
for _ in range(9):
    array.append(int(input()))

array.sort()
man = list(combinations(array, 7))
real_answer = []
for answer in man:
    if sum(answer) == 100:
        real_answer = answer
        break
for real in real_answer:
    print(real)