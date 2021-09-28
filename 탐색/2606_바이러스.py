# DFS를 이용한 풀이

def dfs(graph, v, visited):
    global cnt 
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

n = int(input())
link = int(input())
cnt = 0
com_linked = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(link):
    node1, node2 = map(int, input().split())
    com_linked[node1].append(node2)
    com_linked[node2].append(node1)

dfs(com_linked, 4, visited)

print(cnt)