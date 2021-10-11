### 계수 정렬을 이용한다. ###
## 데이터가 등장한 횟수를 센다.

import sys

n = int(sys.stdin.readline())

arr = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
