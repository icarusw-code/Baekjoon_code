#######0-1 BFS#######
import sys
from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 상근이가 밖에서 문을 열어주는 경우를 고려해야한다.
    visited = [[-1]*(w+2) for _ in range(h+2)] # 맵의 외곽을 추가, 열어야 하는 문의개수
    queue = deque()
    queue.append([x,y])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= h+1 and 0 <= ny <= w+1:
                if visited[nx][ny] == -1:
                    # 문을 안열고 진행
                    if graph[nx][ny] == '.' or graph[nx][ny] == '$':
                        visited[nx][ny] = visited[x][y]
                        queue.appendleft([nx,ny])
                    # 문을 여는 경우
                    elif graph[nx][ny] == '#':
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])
    return visited

for _ in range(t):
    h, w = map(int, input().split())
    graph = [list('.' * (w+2))]
    for i in range(h):
        graph.append(list('.' + input().strip() + '.'))
    graph.append(list('.'*(w+2)))

    prsioner = []
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] == '$':
                prsioner.append([i,j])

    one = bfs(prsioner[0][0], prsioner[0][1])
    two = bfs(prsioner[1][0], prsioner[1][1])
    out_side = bfs(0,0)
    answer = sys.maxsize

    for i in range(h+2):
        for j in range(w+2):
            if one[i][j] != -1 and two[i][j] != -1 and out_side[i][j] != -1:
                result = one[i][j] + two[i][j] + out_side[i][j]
                if graph[i][j] == '*':
                    continue
                if graph[i][j] == '#':
                    result -= 2
                answer = min(answer, result)

    print(answer)