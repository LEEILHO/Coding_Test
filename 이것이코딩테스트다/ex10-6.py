""" 팀결성 학교에서 학생들에게 0번부터 N번까지의 번호 부여 처음에는 모든 학생이 서로 다른 팀으로 구분 되어 N+1 개의 팀이존재
선생님은 팀합치기, 같은팀 여부 확인 연산 사용가능
1. 팀합치키 연산은 두 팀을 합치는 연산
2. 같은팀 여부확인은 특정 두 학생이 같은 팀에 속하는지 확인
M개의 연산을 수행할 때 같은 팀 여부 확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성
n,m n은 입력으로 주어지는 연산의 개수
m 은 각각의 연산이 수행
팀 합치기 연산 0 a b
같은팀 여부 확인 1 a b
같은 팀 여부 확인 연산에 대해 yes no 출력 
"""

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if (a > b):
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i
#연산 차례대로 수행
for i in range(m):
    oper, a,b = map(int,input().split())
    if oper ==0: # 합치기 연산 수행
        union(parent,a,b)
    elif oper ==1: # 팀 여부 확인 수행
        if find_parent(parent,a) ==find_parent(parent,b):
            print("YES")
        else:
            print("NO")