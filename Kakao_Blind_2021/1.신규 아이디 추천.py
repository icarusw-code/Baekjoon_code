def solution(new_id):
    # 1단계
    step_one = new_id.lower()
    # 2단계
    step_two = ''
    for c in step_one:
        if ('a' <= c <= 'z') or ('0'<= c <= '9') or (c == '-') or (c == '_') or (c == '.'):
            step_two += c
    # 3단계
    step_three = ''
    step_three += step_two[0]
    prev = step_two[0]
    for i in range(1, len(step_two)):
        if step_two[i] == '.' and prev == '.':
            continue
        step_three += step_two[i]
        prev = step_two[i]        
    # 4단계
    step_four = step_three.rstrip('.')
    step_four = step_four.lstrip('.')
    # 5단계
    if len(step_four) != 0:
        step_five = step_four
    else:
        step_five = 'a'    
    # 6단계
    step_six = step_five
    if len(step_five) >= 16:
        step_six = step_five[:15]
        if step_six[-1] == '.':
            step_six = step_six[:14]
    # 7단계
    step_seven = step_six
    if len(step_six) == 2:
        step_seven = step_six + step_six[-1]        
    elif len(step_six) == 1:
        step_seven = step_six * 3
        
    return step_seven