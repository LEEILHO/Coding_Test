import sys
N = int(input())
xy = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    xy.append((x,y))

result = sorted(xy, key=lambda x:(x[0] ,x[1]))
for x, y in result:
    print(x, y)