# 가장 긴 바이토닉 부분 수열
# i번째에서 끝나는 가장 긴 증가하는 부분 수열의 길이 
# i번쨰에서 시작하는 가장 긴 증가하는 부분 수열의 길이

n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(i+1 , n):
        if arr[i] > arr[j]:
            dp2[i]= max(dp2[i], dp2[j] + 1)

ans = [dp1[i] + dp2[i] -1 for i in range(n)]
print(max(ans))