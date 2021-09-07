form = input().split("-")

for i in range(len(form)):
    form[i] = form[i].split("+")

total_sum = 0
for i in range(len(form[0])):
    total_sum += int(form[0][i])

for i in range(1, len(form)):
    num_sum = 0
    for j in range(len(form[i])):
        num_sum += int(form[i][j])

    total_sum -= num_sum


print(total_sum)
