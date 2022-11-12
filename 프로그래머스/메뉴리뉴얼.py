from itertools import combinations
def solution(orders, course):
    answer = []
    all_sets=[]
    set_count ={}
    
    for c in course:
        for o in orders:
            sets = combinations(sorted(o),c)
            all_sets += sets
    for sets in all_sets:
        if sets in set_count:
            cnt = set_count[sets]
            cnt +=1
            set_count[sets] = cnt
        else:
            set_count[sets] = 1
    set_count ={key: value for key, value in set_count.items() if value>=2}
    set_count = sorted(set_count.items(), key = lambda x: -x[1])
    # print(set_count)
    for c in course:
        arr =[]
        max_cnt =0
        for s in set_count:
            if len(s[0]) == c:
                if max_cnt <s[1]:
                    arr=[s[0]]
                    max_cnt = s[1]
                elif max_cnt ==s[1]:
                    arr.append(s[0])
        # print(arr)
        for i in arr:
            s = "".join(i)
            answer.append(s)
    answer.sort()
            
            
            
            
    
        
    
    return answer