""" 상하좌우 
L: 왼쪽으로 한칸 R: 오른쪽으로 한칸 U 위로 D 아래로 정사각형을 벗어나는 움직임은 무시된다.
첫쨰줄 공간의 크기 N
둘째 줄 이동할 계획서 내용 
"""
n = int(input())
location = list(map(str, input().split()))
x =1
y =1

for i in range(len(location)):
    if location[i]=='R':
        if(y+1 <= n):
            y +=1
    elif location[i] =='L':
        if(y-1>0):
            y -=1
    elif location[i]=='U':
        if(x-1>0):
            x -=1
    else:
        if (x+1 <=n):
            x +=1
print(x,y)
        
