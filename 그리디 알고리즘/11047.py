n, k = map(int, input().split())
coin_list =[]

for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

def min_coin_count(k):
    count = 0
    for coin in coin_list:
        coin_num = k // coin
        count += coin_num
        k -= coin_num * coin
    return count

print(min_coin_count(k))