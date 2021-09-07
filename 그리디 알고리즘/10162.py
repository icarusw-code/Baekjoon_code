t = int(input())

time = [300, 60, 10]
count = [0] * 3

for i in time:
    count.append(t // i)
    t %= i

if t != 0:
    print(-1)
else:
    for i in count:
        print(i, end = " ")


