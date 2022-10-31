#실패율
#https://school.programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i)
        if length ==0:
            fail =0
        else:
            fail = count/ length
            
        answer.append((fail,i))
        length -=count
        
        
    answer = sorted(answer, key= lambda x: -x[0])
    answer = [i[1] for i in answer]
    return answer