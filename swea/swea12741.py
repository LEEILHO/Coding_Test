#swea12741 두 전구
T = int(input())
#결과 출력용 리스트
result = []

for test_case in range(1, T + 1):
    A,B,C,D = map(int,input().split())
    if min(B,D)-max(A,C)>0: # 동시에 켜지는 시간은 두개의 시작시간의 최대값을 꺼지는 시간 최소값에 빼서 0보다 크면 동시에 켜있는 시간
        result.append(min(B,D)-max(A,C)) 
    else:
        result.append(0)
for i in range(len(result)):
    print("#{} {}".format(i+1,result[i]))
