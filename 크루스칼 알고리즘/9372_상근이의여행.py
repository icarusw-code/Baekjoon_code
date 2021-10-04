t = int(input())

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

for _ in range(t):
    n, m = map(int, input().split())
    nations = [0] * (n+1)
    count = 0

    for i in range(1, n+1):
        nations[i] = i
    
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(nations, a) != find_parent(nations, b):
            union_parent(nations, a, b)
            count += 1
    
    print(count)