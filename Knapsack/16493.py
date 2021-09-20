n, chapter = map(int, input().split())

dy = [0] *(n+1)

for i in range(chapter):
    day, page = map(int, input().split())
    for j in range(n, day-1, -1):
        dy[j] = max(dy[j], dy[j-day]+page)
    
print(dy[n])
