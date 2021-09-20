N, K = map(int, input().split())
dy = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W-1, -1):
        dy[i] = max(dy[i], dy[i-W] + V)

print(dy[K])