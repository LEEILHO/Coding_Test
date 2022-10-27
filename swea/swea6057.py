#그래프의 삼각형
#https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AWbHcWd6AFcDFAV0&categoryId=AWbHcWd6AFcDFAV0&categoryType=CODE
T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[]for _ in range(n+1)]
    
    for i in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    count =0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            for k in range(j+1, n+1):
                if i in graph[j] and j in graph[k] and k in graph[i]:
                    count+=1
    print(f"#{tc} {count}")
    