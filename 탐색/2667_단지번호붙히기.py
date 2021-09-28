n = int(input())
graph = []
cnt = 0 
house = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            house.append(cnt)
            cnt = 0

print(len(house))
house.sort()
for i in house:
    print(i)


