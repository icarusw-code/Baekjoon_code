# 이 문제는 비트마스킹 + DP + DFS 를 모두 활용하는 문제로 난이도가 있는 문제이다.

 

# 각 도시를 방문했는지의 여부는 비트마스킹( 0001, 0002 ... 1111 )을 활용하고

# 현재 도시에서의 최소비용은 DP를 활용하고

# 도시를 방문하는 것은 DFS를 활용한다.

 

# ① 먼저, 출발도시를 정해야 한다.

# 나는 0번 도시를 출발지점으로 정했는데, 어느 도시를 출발지점으로 정하든지 상관이 없다.

# 문제에서, 그래프는 순환경로(싸이클)를 이루기 때문에

# 만약, 1 -> 0 -> 3 -> 2 -> 1 경로가 최소 비용 경로라면

# 0 -> 3 -> 2 -> 1 -> 0 도 최소 비용 경로가 되기 때문이다.

# 즉, 출발점 1 에서 최소 비용 경로가 존재할 때, 0에서도 같은 경로가 반드시 존재하게 된다.

 

# ② 거친 도시를 비트마스킹으로 표시한다.

# visited라는 변수에 2진수로 거친 도시를 표시하였다.

 

# visited에 다음과 같이 값을 할당한다.

# 0001(2) = 1 이라면 => 0번 도시만을 거침

# 0011(2) = 3 이라면 => 0, 1 번 도시를 거침

# 1111(2) = 15 이라면 => 0, 1, 2, 3 번 도시를 거침

# 이렇게 어느 도시들을 거쳤는지 거치지 않았는지를 비트마스크로 표시하였다.

 

# ③ dp에는 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용이 저장된다.

# dp[cur][visit] = 현재 cur도시이며 방문현황은 visit과 같고, 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용

 

# 점화식이 잘 이해가 가지 않는다면,

# 뒤에서 부터 생각하면 좀 더 이해하기 쉬울 것이다.

# dp[next][nextvisit]이 next도시에서 남은 도시를 거쳐 시작점으로 돌아가는 최소비용이기 때문에

# dp[cur][visit]은 dp[next][nextvisit]보다 graph[cur][next]만큼의 비용이 더 들 것이다.

# 즉, 다음 지점의 dp보다 다음 지점으로 가는데에 드는 비용만큼 더 들게 되는 것이다.

 

# 예를 들어, dp[0][0011(2)] = dp[0][3]은 현재 0번 도시이며, 0, 1번 도시를 방문하였고, 2, 3을 방문한 후 다시 시작점으로 돌아갈 때의 최소 비용이며

# dp[2][0111(2)] = dp[2][7]은 현재 2번 도시이며 0,1,2 번 도시를 방문하였으며, 3을 방문한 후 다시 시작점으로 돌아갈 때의 최소비용이다.

# 즉, dp[0][0011] = dp[2][0111] + graph[0][2]이 되는 것이다.

 

# 이를 점화식으로 나타내면 다음과 같다.

# dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])

 

# ④ DFS를 통해 DP값을 갱신시켜 준다.

# dp[next][visited | (1<<next)] 부분을

# dfs(next, visited | (1<<next) ) 를 통해 재귀함수를 돌리며 DP값을 갱신시켜준다.

 

# 위 방식을 파이썬으로 나타낸 코드는 다음과 같다.


n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))