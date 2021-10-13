n = int(input())
graph = []
cnt = 0
house = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
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


# BFS

from collections import deque

n = int(input())
apt = []
for i in range(n):
    apt.append(list(map(int, input())))
visit = [[0] * n for i in range(n)]  # 1
dx = [-1, 0, 1, 0]  # 2
dy = dx[::-1]


def bfs(x, y, idx):
    q = deque([[x, y]])  # 6
    visit[x][y] = 1
    while q:
        node = q.popleft()
        for i in range(4):
            nx = node[0] + dx[i]  # 7
            ny = node[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 8
                if apt[nx][ny] == 1 and visit[nx][ny] == 0:  # 9
                    q.append([nx, ny])  # 10
                    visit[nx][ny] = 1  # 11
                    apt_list[idx] += 1  # 12


apt_list = {}
idx = 0
for i in range(n):  # 3
    for j in range(n):
        if apt[i][j] != 0 and visit[i][j] == 0:  # 4
            apt_list[idx] = 1  # 5
            bfs(i, j, idx)
            idx += 1  # 13
apt_list = sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)
