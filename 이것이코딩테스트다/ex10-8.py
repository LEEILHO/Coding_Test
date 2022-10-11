"""커리 큘럼 동빈이는 강의를 듣는데 선수강의가 있을 수 있다.
선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
N개의 강의 1번부터 N번의 번호 동시에 여러가지 강의를 들을수 있다 가정 
강의의수 N
강의 시간 강의를 득기 위해 먼저 들어야하는 강의들의 번호가 자연수 각자연수는 공백으로 구분
최소시간은?
"""
n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

time = [0] * (n+1)

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)
from collections import deque
import copy

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] ==0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now] + time[i]) 
            indegree[i] -=1
            if indegree[i] ==0:
                q.append(i)
    for i in range(1,n+1):
        print(result[i])
topology_sort()