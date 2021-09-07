n = int(input())
meeting = []

for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting = sorted(meeting, key = lambda x: [x[1], x[0]])

count = 0
start = 0 
for meet in meeting:
    if meet[0] >= start:
        start = meet[1]
        count += 1

print(count)