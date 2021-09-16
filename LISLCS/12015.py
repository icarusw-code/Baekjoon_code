from bisect import bisect_left
# 1. dp를 arr[0]으로 초기화한다.
# 2. 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다.
# 3. 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다. 그리고 dp의 index 원소를 arr[i]로 바꿔준다.
# 4. dp의 길이를 출력한다.

n = int(input())
arr = list(map(int, input().split()))

# dp 는 가장 긴 증가하는 부분 수열을 저장할 배열
dp = [arr[0]] # dp 를 arr[0]으로 초기화

for i in range(n):
  	# 현재 위치(i) 가 이전 위치의 원소들보다 크면 dp 에 추가한다.
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        # 자신보다 큰 수 중 최솟값과 대치(이진탐색 이용)
        # 10 20 30 25 50 으로 하면 이해하기 쉬움 
        # 뒤에 더 긴 길이를 만들기위해 값을 갱신해줌
        dp[bisect_left(dp, arr[i])] = arr[i]
        
print(len(dp))