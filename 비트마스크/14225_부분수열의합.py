n = int(input())
arr = list(map(int, input().split()))
check = [False] * (20 * 100000)

for i in range(1<<n):
    sum = 0
    for j in range(n):
        if (i & (1<<j)):
        # arr = [5, 1 ,2]
        # 0,1,2 에 해당하는 인덱스의 원소값을 하나씩 더해줌
        # sum에서 6이 나오는 이유는 sum +arr[0]+ arr[1] 한 결과
            sum += arr[j]
    check[sum] = True
# 자연수 이므로
i = 1
while True:
    if check[i] == False:
        break
    i += 1

print(i)