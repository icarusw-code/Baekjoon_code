def solution(str):
    dic = {
        "zero" : "0", "one":"1", "two":"2",
        "three":"3", "four":"4", "five":"5",
        "six":"6", "seven":"7", "eight":"8",
        "nine":"9"
        }

    answer = str
    for key, value in dic.items():
        answer = answer.replace(key, value)
    
    return int(answer)

    # # 바로 넣어주기
    # num = []
    # # 하나씩 넣어주기
    # string = ""
    
    # for s in str:
    #     if s.isalpha():
    #         string += s
            
    #         if string in dic:
    #             num.append(dic[string])
    #             string = ""
            
    #     else:
    #         num.append(s)
            
    # answer = int("".join(num))
    # return answer