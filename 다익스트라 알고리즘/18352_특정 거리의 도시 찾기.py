import heapq

INF = 2147000000
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cost = [INF] * (N + 1)
heap = []

def dijkstra(start):
    heapq.heappush(heap, [0, start])
    cost[start] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        for n, d in graph[now]:
            dw = d + dist
            if dw < cost[n]:
                cost[n] = dw
                heapq.heappush(heap, [dw, n])

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

dijkstra(X)

ans = []
for i in range(1, N+1):
    if cost[i] == K:
        ans.append(i)
if ans:
    for i in ans:
        print(i)
else:
    print(-1)