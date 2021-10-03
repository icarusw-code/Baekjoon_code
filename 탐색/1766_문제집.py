## 위상정렬의 개념을 사용
## 순서가 정해져 있는 작업이 있을때 ----> 순서를 결정해주는 알고리즘
#########위상 정렬###########

# 1. 진입 차수가 0인 정점을 큐에 삽입
# 2. 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 3. 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
# 4. 큐가 빌때까지 2-3 과정을 반복

import heapq

n, m = map(int, input().split())
array = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

heap = []
result = []

for _ in range(m):
    x, y = map(int, input().split())
    array[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -= 1
        if indegree[y] ==0:
            heapq.heappush(heap, y)

for i in result:
    print(i, end=' ')