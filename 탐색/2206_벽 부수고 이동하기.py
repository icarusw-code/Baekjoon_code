from collections import deque

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input())))

# BFS 알고리즘을 순환하면서, 벽을 뚫을 수 있는 상태이고, 
# 벽을 만난다면 벽을 뚫어주고 + 1을 해준다. 
# 아직 방문하지 않았고 벽이 아니라면 + 1을 해준다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    # visted[x][y][w] w가 0이면 벽을 뚫은 상태/ 1이면 벽을 뚫을 수 있는 상태
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 만나고 , 벽을 부술 수 있는경우
                if board[nx][ny] == 1 and w == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append([nx, ny , 0])
                # 벽이 없고, 방문한적이 없는 경우 
                elif board[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1

print(bfs())