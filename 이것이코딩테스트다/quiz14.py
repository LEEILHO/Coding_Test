""" 외벽 점검
레스토랑을 직접 리모델링
공사중에 주기적으로 외벽의 상태를 점검해야함
구조는 완전히 동그란 모양이고 총 둘레는 N미터이며추위가 심할 경우 손상 될수 도 있는 취약지점들이 있다
내부 공사 도중에는 외벽의 취약지점들이 손상되지 않았는지 주기적으로 점검
점검 시간을 1시간으로 제한 친구들이 1시간동안 이동 할 수 있는 거리는 제각각
최소한의 친구들을 투입해 취약 지점을 점검 나머지 친구들은 내부 공사 정북 방향 지점을 0으로 나타내며 취약 지점의 위치는 정북 방향 지점부터 
시계 방향으로 떨어진 거리 친구들은 출발 지점 부터 시계 혹은 반 시계 방향으로 외벽을 따라서 이동
외벽의 길이 n 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dict로 매개변수로 주어질 때
취약 지점을 점검하기 위해 보내야 하는 친구 수 return 하도록 solution"""
from itertools import permutations
def solution(n,weak,dict):
    #길이를 2배로 늘려서 '원형'을 일자 형태로 변경
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dict) +1
    #0부터 lenght-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        #친구를 나열하는 모든 경우의 수 각각에 대해 확인
        for friends in list(permutations(dict,len(dict))):
            count =1
            #해당 친구가 점검할 수 있는 마지막 위치
            poisition = weak[start] + friends[count-1]
            # 시작점부터 모든 취약지점을 확인
            for index in range(start, start+length):
                #점검위치를 벗어나는 경우
                if poisition < weak[index]:
                    # 인원 추가
                    count+=1
                    # 더 투입이 불가능하면 종료
                    if count >len(dict):
                        break
                    poisition = weak[index] + friends[count-1]
            answer = min(answer,count)
    if answer > len(dict):
        return -1
    return answer
    