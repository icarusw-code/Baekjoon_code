n = int(input())
edges = []


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n):
    edges.append(list(map(int, input().split())))

parent = [0] * (n + 1)
for i in range(n):
    parent[i] = i

arrays = []

for i in range(n):
    for j in range(i + 1, n):
        arrays.append((edges[i][j], i, j))

arrays.sort()
result = 0
for array in arrays:
    cost, a, b = array
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost

print(result)
