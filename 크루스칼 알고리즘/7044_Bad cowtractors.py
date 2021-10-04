def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [-1] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=True)
result = 0
cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        cnt += 1
#### 최소신장트리가 이루어지지 않는경우 5개 노드중에 3개 / 2개 이런식으로 되어있는경우 예외처리
if cnt == n-1:
    print(result)
else:
    print(-1)