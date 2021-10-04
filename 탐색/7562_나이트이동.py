from collections import deque
t= int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    count = [[0]*n for _ in range(n)]

    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]

    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if count[nx][ny] == 0:
                count[nx][ny] = count[x][y] + 1
                queue.append((nx,ny))
    print(count[end_x][end_y])

