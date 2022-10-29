#햄버거 다이어트

def dfs(idx,score,cal):
    global best_score
    
    if cal > l:
        return
    if score > best_score:
        best_score = score
    if idx ==n:
        return
    
    dfs(idx+1,score,cal)
    dfs(idx+1,score+arr[idx][0],cal+arr[idx][1])
T = int(input())

for tc in range(1,T+1):
    n,l = map(int, input().split())
    arr =[]
    best_score = 0
    score=0
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    dfs(0,0,0)
    print('#{} {}'.format(tc, best_score))
