from bisect import bisect_left
from typing import OrderedDict

n = int(input())
arr = [0] + list(map(int,input().split())) # input
dp = [0] * (n+1) # for memoization
cmp = [-1000000001] # 이진탐색을 위해 생성.
order = 0 #최대값을 저장할 변수

for i in range(1, n+1): #arr 반복 실행.
    if cmp[-1] < arr[i]: #이진탐색으로 저장된 값들은 정렬되므로 맨 뒤의 값 비교.
        cmp.append(arr[i])
        dp[i] = len(cmp) - 1
        order = dp[i]
    else:
        dp[i] = bisect_left(cmp, arr[i]) #현재 값이 어느 위치의 값에 해당하는지 비교.
        cmp[dp[i]] = arr[i] #cmp 업데이트.
print(order) #최대 길이 출력

res = []
for i in range(n, 0, -1):
    if dp[i] == order:
        res.append(arr[i])
        order -= 1
        
print(*res[::-1])