from collections import deque

n = int(input())
start_x, start_y, end_x, end_y = map(int, input().split())
count = [[0] *n for _ in range(n)]

dx = [-2, -2, 0, 0, +2, +2]
dy = [-1, +1, -2, +2, -1, +1]

def bfs(x, y):
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if count[nx][ny] == 0:
                count[nx][ny] = count[x][y] + 1
                queue.append((nx, ny))
    return count[end_x][end_y]

result = bfs(start_x, start_y)

if result != 0:
    print(result)
else:
    print(-1)
