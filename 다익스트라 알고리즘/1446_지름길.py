n, d = map(int, input().split())

road = []
for i in range(n):
    start, end, length = map(int, input().split())
    if end <= d:
        road.append([start, end, length])

distance = [i for i in range(d+1)]

for j in range(d+1):
    if j != 0:
        distance[j] = min(distance[j], distance[j-1] + 1)
    for i in road:
        if i[0] == j:
            distance[i[1]] = min(distance[i[1]], distance[i[0]] + i[2])

print(distance[d]) 

# # 지름길 (건호)

# n, d = map(int, input().split())

# shortcut = [list(map(int, input().split())) for _ in range(n)]
# distance = [i for i in range(d+1)]

# for i in range(d+1):
#     if i > 0:
#         distance[i] = min(distance[i], distance[i-1]+1)
#     for start, end, dist in shortcut:
#         if i == start and end <= d and distance[start] + dist <= distance[end]:
#             distance[end] = distance[start] + dist

# print(distance[d])