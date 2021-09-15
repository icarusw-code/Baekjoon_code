import sys
n = int(input())
count = [0] * 10001

for _ in range(n):
    index = (int(sys.stdin.readline()))
    count[index] += 1

for i in range(len(count)):
    if count[i]:
        for j in range(count[i]):
            print(i)

        