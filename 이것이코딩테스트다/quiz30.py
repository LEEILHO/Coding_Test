#가사 탐색 
#https://school.programmers.co.kr/learn/courses/30/lessons/60060
def find_first(word,left,right,x):
    if left > right :
        return None
    mid = (left+right)//2
    if len(word)==1:
        if word[0][0:len(x)] ==x:
            return 0
        else:
            return None
    
    if (word[mid][0:len(x)] == x and word[mid-1][0:len(x)] < x ) or (word[mid][0:len(x)] == x and mid ==0):
        return mid
    if word[mid][0:len(x)] >= x:
        return find_first(word,left,mid-1,x)
    if word[mid][0:len(x)] <x:
        return find_first(word,mid+1,right,x)
            
def find_last(word,left,right,x):
    if left > right:
        return None
    if len(word)==1:
        if word[0][0:len(x)] ==x:
            return 0
        else:
            return None       
    mid = (left+right)//2
    if word[mid][0:len(x)] == x and mid +1 == len(word):
        return mid
    if word[mid][0:len(x)] == x and word[mid+1][0:len(x)] > x :
        return mid
    if word[mid][0:len(x)] <=x:
        return find_last(word,mid+1,right,x)
    if word[mid][0:len(x)] > x:
        return find_last(word,left,mid-1,x)
def count_by_index(left,right):
    if left ==None or right ==None:
        return 0
    else:
        return right - left + 1


def solution(words, queries):
    
    word = [[]  for _ in range(10001)]
    reversed_word = [[]  for _ in range(10001)]
    for i in words:
        word[len(i)].append(i)
        reversed_word[len(i)].append(i[::-1])
    for i in range(10001):
        word[i].sort()
        reversed_word[i].sort()
        
    answer = []
    for q in queries:
        query = ""
        #접미사 ?
        if q[0] == '?' and q[-1] =='?':
            answer.append(len(word[len(q)]))
        else:
            
            
            if  q[0] !='?':
                for j in q:
                    if j !="?":
                        query+=j
                    else:
                        break
                first_index = find_first(word[len(q)],0, len(word[len(q)])-1,query)
                last_index = find_last(word[len(q)],0, len(word[len(q)])-1,query)

            #접두사 ?
            if q[-1] !="?":

                for j in range(len(q)-1,-1,-1):
                    if q[j] !="?":
                        query+=q[j]
                    else:
                        break
                first_index = find_first(reversed_word[len(q)],0,len(reversed_word[len(q)])-1,query)
                last_index = find_last(reversed_word[len(q)],0,len(reversed_word[len(q)])-1,query)
            answer.append(count_by_index(first_index,last_index))
            
                
                
            
    return answer
