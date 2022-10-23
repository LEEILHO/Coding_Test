# 다솜이의 월급 상자
T = int(input())

for tc in range(1,T+1):
    n = int(input())
    result =0
    for _ in range(n):
        data = input().split()
        pi = float(data[0])
        xi = int(data[1])
        result += pi *xi
    print("#{} {:.6f}".format(tc,result))