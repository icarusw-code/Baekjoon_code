from collections import deque

checker = True
m, n = list(map(int, input().split()))
tomato = [] 
for _ in range(n):
    tomato.append(list(map(int, input().split())))

q = deque() # 익은 토마토를 담을 큐 생성

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1: #익은 토마토 큐에 추가
            q.append([i,j])

dx = [-1, 1, 0 ,0]
dy = [0, 0 ,-1, 1]

time = -1 # 걸린 날짜 만약, 이미 다 익은 토마토인 경우에는 날짜 0을 리턴하기 위함

def bfs(q, time):
    while q:
        time += 1
        for _ in range(len(q)): # 큐의 길이만큼 반복, 익은 토마토가 여러개 일 수 도 있으니까
            x, y = q.popleft()
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 안에 있고 안익은 토마토 인 경우 큐에 넣어주고 익혀준다
                if (0 <= nx < n) and (0 <= ny < m) and tomato[nx][ny] ==0:
                    q.append([nx,ny])
                    tomato[nx][ny] = 1
    return time

time = bfs(q, time)

for i in tomato:
    if 0 in i:
        checker = False
        print(-1)
        break

if checker:
    print(time)
