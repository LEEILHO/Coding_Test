#카드 제거
from collections import deque
def check(cards):
    if cards.count('0') ==0:
        return True
    else:
        return False
        
    
T = int(input())
for tc in range(1,T+1):
    S = input()
    cards= [2]
    for i in S:
        cards.append(i)
    length = len(cards)
    result ="yes"
    if cards.count('1')==0:
        result = 'no'
    else:
        q = deque()
        for card in range(length):
            if cards[card] =="1":
                q.append(card)
        while q:
            now = q.popleft()
            if cards[now] =="1":
                cards[now] = "2"
                prev, next = now-1,now+1
                if prev > 0 :
                    if cards[prev] =="0":
                        cards[prev] ="1"
                        q.append(prev)
                    elif cards[prev] =="1":
                        cards[prev] =="0"
                
                if next < length:
                    if cards[next] =="0":
                        cards[next] ="1"
                        q.append(next)
                    elif cards[next] == "1":
                        cards[next] ="0"
    if result =="yes":
        if check(cards) == False:
            result = "no"
    print(f"#{tc} {result}")

    
                        
                
            
        
    
        
    
        
    
    
    