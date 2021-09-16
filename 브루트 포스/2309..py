# 1 2 3 4 5 6 7 8 9 
# 2명을 뺐을때 합이 100이 되면 그 두명을 제외

tall = [int(input()) for i in range(9)]
# for i in range(9):
#     tall.append(int(input()))

sum_tall = sum(tall)

for i in range(len(tall)):
    for j in range(i+1, len(tall)):
        if sum_tall - (tall[i] + tall[j]) == 100:
            num1, num2 = tall[i], tall[j]

            tall.remove(num1[i])
            tall.remove(num2[j])
            tall.sort()

            for i in range(len(tall)):
                print(tall[i])
            # 리스트에서 원소를 제거하였으면 탈출을 해줘야 out of range 오류가 안생김
            break

    if len(tall) < 9:
        break