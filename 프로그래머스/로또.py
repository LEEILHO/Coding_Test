#https://school.programmers.co.kr/learn/courses/30/lessons/77484

def rank(correct):
    if correct ==6:
        return 1
    elif correct ==5:
        return 2
    elif correct ==4:
        return 3
    elif correct ==3:
        return 4
    elif correct ==2:
        return 5
    else:
        return 6
def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    correct_cnt =0
    for i in lottos:
        if i ==0:
            zero_cnt +=1
        else:
            if i in win_nums:
                correct_cnt +=1
    answer.append(rank(correct_cnt+zero_cnt))
    answer.append(rank(correct_cnt))
    
            
    
    
    return answer