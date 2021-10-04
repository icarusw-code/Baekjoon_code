from collections import deque


def bfs(start):
    visited =[False] * (n+1)    
    queue = deque([start])
    visited[start] =True
    check = [1]
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                check.append(i)
    return check

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

now = list(map(int, input().split()))
order = [0] * (n + 1)

for i in range(len(now)):
    order[now[i]] = i

for i in range(1, len(graph)):
    graph[i].sort(key = lambda x:order[x])

check = bfs(1)

if now == check:
    print(1)
else:
    print(0)
    