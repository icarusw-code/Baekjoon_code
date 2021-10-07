# 1. 상어가 먹을 수 있는 물고기를 찾는다. (BFS 를 이용)
# 2. 이동해서 먹는다.
import sys
from collections import deque

INF = sys.maxsize

n = int(input())
array = []
shark_size = 2
now_x, now_y = 0, 0

for i in range(n):
    array.append(list(map(int, input().split())))

# 상어를 찾아서 0으로 표시하고 위치를 저장
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

# 상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 최단 거리 테이블 만들기
def bfs():
    # 값이 -1이면 도달할 수 없다는 의미
    distance = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하며 값은 0
    queue = deque([(now_x, now_y)])
    distance[now_x][now_y] = 0

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:  # 범위 안에 있다면
                if distance[nx][ny] == -1 and array[nx][ny] <= shark_size:
                    # 물고기가 상어보다 작거나 같으면 이동 가능
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
    return distance


def find(distance):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달할 수 있고 먹을 수 있는 물고기라면
            if distance[i][j] != -1 and array[i][j] >= 1 and array[i][j] < shark_size:
                if min_dist > distance[i][j]:
                    x, y = i, j
                    min_dist = distance[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0

while True:
    # 가장 가까운 물고기 찾기
    value = find(bfs())
    if value == None:  # 물고기가 없다면 현재까지 시간을 리턴
        print(result)
        break
    else:  # 물고기가 있다면
        # 현재 위치, 시간을 재설정하고 물고기 먹기
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        # 먹은 물고기 크기가 현재 상어 크기보다 크거나 같다면
        if ate >= shark_size:
            shark_size += 1
            ate = 0
