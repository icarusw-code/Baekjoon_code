n = int(input())

# 단백질, 지방, 탄수화물, 비타민 최소
target = list(map(int, input().split()))

nutrient = []
# 각 영양소 
for _ in range(n):
    nutrient.append(list(map(int, input().split())))

result_cost = 1e9
answers = []
num_list = []

# 모든 경우의 수
for i in range(1 << n):
    cur_p, cur_f, cur_s, cur_v, cur_cost = 0, 0, 0, 0, 0
    for j in range(n):
        # 해당 경우의수 일때 
        if i&(1 << j):
            cur_p += nutrient[j][0]
            cur_f += nutrient[j][1]
            cur_s += nutrient[j][2]
            cur_v += nutrient[j][3]
            cur_cost += nutrient[j][4]
         
        
    if cur_p >= target[0] and cur_f >= target[1] and cur_s >= target[2] and cur_v >= target[3]:
            if result_cost > cur_cost:
                result_cost =cur_cost
                answers = []
                answers.append(i)
                # answers.append(bin(i))

            elif result_cost == cur_cost:
                answers.append(i)
                # answers.append(bin(i))

print(answers)

if result_cost == 1e9:
    print(-1)

else: 
    answers.sort()
    answer = answers[0]
    index = -1 
    # while True:
    #     index = answer.find('1', index +1)
    #     if index == -1:
    #         break
    #     num_list.append(index)

    # print(result_cost)
    # print(*num_list)        
