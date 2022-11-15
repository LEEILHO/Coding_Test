#3975 승률 비교하기
T = int(input())
result =[]
for tc in range(1,T+1):
    A,B,C,D = map(int, input().split())
    Alice = A/B
    Bob = C/D
    if Alice>Bob:
        result.append("ALICE")
    elif Alice< Bob:
        result.append("BOB")
    else:
        result.append("DRAW")
for i in range(len(result)):
    print("#{} {}".format(i+1,result[i]))