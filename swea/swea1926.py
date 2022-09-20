#간단한 369게임
N = int(input())
for i in range(1,N+1):
    cnt = 0
    cnt +=str(i).count('3') #3이들어가는 횟수
    cnt +=str(i).count('6') # 6이 들어가는 횟수
    cnt += str(i).count('9') #9가 들어가는 횟수
    if cnt ==0: #cnt값이 0이면 수 그대로 출력
        print(i, end = ' ')
    else:
        print(cnt*'-', end = ' ') # cnt값이 1이상이면 cnt만큼 -출력
    