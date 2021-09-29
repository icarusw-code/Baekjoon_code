# import heapq
# # 정점 n / 간선 m 
# n, m = map(int, input().split())
# INF = 1e9
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# # p 집의 후보지 개수 / q 편의점의 개수
# p, q = map(int, input().split())
# house = list(map(int, input().split()))
# cu = list(map(int, input().split()))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost <distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# dijkstra(1)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         if i in cu:
#             print(distance[i])
#             exit()