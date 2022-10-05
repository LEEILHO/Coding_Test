"""시각
정수 N 입력 00시 00분 00초 부터 N시 59분 59초 까지 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의수를 구하는 프로그램
첫째줄 정수 N:0이상 23이하
"""
n = int(input())
cnt =0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s) :# 3이 포함되어있으면 cnt ++
                cnt +=1
print(cnt)