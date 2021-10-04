from collections import deque

start, end = map(int, input().split())
dist = [0] * 100001

def bfs(start, end):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == end:
            print(dist[v])
            break

        for nv in (v-1, v+1, v*2):
            if 0 <= nv <= 100000 and not dist[nv]:
                dist[nv] = dist[v] + 1
                queue.append(nv)

bfs(start, end)            