from collections import deque

def bfs(start):
    queue = deque([start])
    check[start] = 0
    while queue:
        start = queue.popleft()
        for i in range(1, 7):
            n = start + i
            if n > 100:
                continue
            next_node = graph[n]
            if check[next_node] == -1:
                queue.append(next_node)
                check[next_node] = check[start] + 1
                if next_node == 100:
                    return check[100]



n, m = map(int, input().split())

graph = [i for i in range(101)]

for _ in range(n):
    u, v = map(int, input().split())
    graph[u] = v

for _ in range(m):
    u, v = map(int, input().split())
    graph[u] = v

check = [-1] * 101

# bfs(1)
# print(check[100])

print(bfs(1))