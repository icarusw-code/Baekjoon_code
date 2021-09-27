n = int(input())
data = [0]
result = [0] * (n + 2)
for i in range(1, n+1):
    t, p = map(int, input().split())
    data.append((i,t,p))
# 날짜, 소요시간, 페이
#[0, (1, 3, 10), (2, 5, 20), (3, 1, 10), (4, 1, 20), (5, 2, 15), (6, 4, 40), (7, 2, 200)]

for i in range(1, n+1):
    day, time, pay = data[i]
    if day + time <= n+1:
        result[i] += pay
        # 뒤에 result 값들도 최산화
        for j in range(day+time, n+1):
            result[j] = max(result[day], result[j])

print(max(result))