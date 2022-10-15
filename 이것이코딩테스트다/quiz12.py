""" 기둥과 보
조르디는 인생 2막을 위해 주택 건축 사업에 뛰어들기로 결심하였다.
기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획
그에 맞는 시뮬레이션 할 수 있는 프로그램을 만들고 있다.
규칙 1. 기둥은 바닥 윙에 있거나 보의 한쪽 끝부분 위에 있거나 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야함.
벽면의 크기 N 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개 변수로 주어질 떄
모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 작성하시오
n  5이상 100이하
build_frame 1이상 1000이하 가로열 4
[x,y,a,b]: x,y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며 [가로,세로]형태
a는 설치 혹은 삭제할 구조물의 종류 0은 기둥 1은 보
b는 설치 혹은 삭제 0은 삭제 1설치
구조물은 교차점 기준 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제
"""
def check(answer):
    for x,y, stuff in answer:
        if stuff==0: #기둥이라면
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer: # 땅위에 있거나,보의 한쪽 부분 끝 혹은 다른 기둥 위
                continue
            return False
        elif stuff==1: #보라면
            #    왼쪽부분 기둥위       오른쪽 부분 기둥위           왼쪽부분 보    오른쪽 부분 보 둘다 연결
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer): 
                continue
            return False
    return True


def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        x,y, stuff,operate = frame
        if operate ==0:
            answer.remove([x,y,stuff]) # 삭제 진행
            if  check(answer) == False: #삭제가 불가능하면 다시 추가
                answer.append([x,y,stuff])
        if operate ==1:
            answer.append([x,y, stuff])
            if check(answer) == False:  #추가 불가능하면 다시 삭제
                answer.remove([x,y,stuff])
    return sorted(answer)
