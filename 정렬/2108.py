import sys
from typing import Counter
from collections import Counter

n = int(input())

array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

# 1번 조건
mean = round(sum(array)/n)
print(mean)

# 2번 조건
array.sort()
middle = array[n//2]
print(middle)

# 3번 조건
most_num = Counter(array).most_common()

if len(most_num) > 1 and most_num[0][1] == most_num[1][1]:
    print(most_num[1][0])
else:
    print(most_num[0][0])

# 4번 조건
length = max(array) - min(array)
print(length)