import sys
from collections import deque
import pprint

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
board = []
for i in range(h):
    board.append(list(map(int, input().split())))

h_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dy = [-2, -1, 1, 2, -2, -1, 1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


visited = [[[0 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]


def bfs(x, y):
    queue = deque()
    # 나이트 처럼 움직인 횟수 k
    queue.append((x, y, k))
    while queue:
        x, y, z = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and board[nx][ny] != 1
                and visited[nx][ny][z] == 0
            ):
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
        if z > 0:
            for i in range(8):
                nx = x + h_dx[i]
                ny = y + h_dy[i]
                if (
                    0 <= nx < h
                    and 0 <= ny < w
                    and board[nx][ny] != 1
                    and visited[nx][ny][z - 1] == 0
                ):
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z - 1))
    return -1


pprint.pprint(visited)
pprint.pprint(board)
print(bfs(0, 0))
