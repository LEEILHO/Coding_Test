# 몬스터 사냥
T = int(input())
for tc in range(1,T+1):
    d,l,n = map(int,input().split())
    result = n*d + d*l*n*(n-1)/200
    print("#{} {}".format(tc,result))