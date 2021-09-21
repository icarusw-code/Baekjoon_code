import heapq
start, end = map(int, input().split())
# 노드 n개, 간선 수 m개
n, m = map(int, input().split())

INF = 2147000000
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijksrta(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijksrta(start)

if distance[end] == INF:
    print(-1)
else:
    print(distance[end])
