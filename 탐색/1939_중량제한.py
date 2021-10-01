import sys
from collections import deque

n,m = map(int, input().split())
road =[[] for _ in range(n+1)]

def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        a = queue.popleft()
        for b, weight in road[a]:
            if not visited[b] and weight >= c:
                visited[b] = True
                queue.append(b)
    return visited[end_node]

start = sys.maxsize
end = 1

for _ in range(m):
    a, b, weight = map(int, input().split())
    road[a].append((b, weight))
    road[b].append((a, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start

while (start <= end):
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)