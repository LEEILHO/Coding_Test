from itertools import combinations
def solution(relation):
    answer =0
    length = len(relation)
    candidate =[]
    for i in range(1,len(relation[0])+1):
        candidate.extend(combinations(range(len(relation[0])),i))
    
    unique = []
    for c in candidate:
        tmp = [ tuple ([item[i] for i in c ]) for item in relation]
        if len(set(tmp)) == length:
            unique.append(c)
    answer = set(unique)
    print(set(unique))
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                
            
            
            
    return len(answer)