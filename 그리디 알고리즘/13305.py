n = int(input())
road = list(map(int, input().split()))
gas_cost = list(map(int, input().split()))

total_cost = 0
min_gas_cost = gas_cost[0]

for i in range(len(road)):
    total_cost += road[i] * min_gas_cost
    if min_gas_cost > gas_cost[i + 1]:
            min_gas_cost = gas_cost[i + 1]

print(total_cost)



