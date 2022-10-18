""" 괄호 변환
콘은 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무과제
분석 결과 작성한 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 경우가 대부분
용어 ()의 개수가 같다면 균형잡힌  괄호 문자열 
(()))(는 균형잡인 괄호 이지만 올바른 괄호는 아님
1. 입력이 빈 문자열인 경우 빈 문자열을 반환
2. 문자열 w를 두 균형잡힌 괄후 문자열 u,v로 분리 단 U는 균형잡인 괄호 문자열로 더이상 분리 x v는 빈 문자열이 될 수 있다
3. 수행한 결과 문자열을 u에 이어 붙인 후 반환
    3-1 문자열 u가 올바른 괄호 문자열이면 v에 대해 1단계부터 다시 수행
4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정 수행
    4-1. 빈 문자열에 첫번째 문자로 ( 붙임
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
    4-3. )를 다시 붙임
    4-4 u의 첫번째와 마지막 문자를 제거 나머지 문자열의 괄호 방향을 뒤집에서 뒤에 붙인다
    4-5 생성된 문자열 반환"""

# 균형잡인 괄호 문자열의 인덱스 반환
def balanced_index(p):   
    count =0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] =='(':
            count +=1
        else:
            count -=1
        if count == 0:
            return i
def chekc_proper(p):
    count =0
    for i in p:
        if i =='(':
            count +=1
        else:
            if count ==0:
                return False
            count -=1
    



def solution(p):
    answer = ''
    if p =='':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    if chekc_proper(u):
        answer = u +solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for i in range(len(u)):
            if u[i] =='(':
                u[i] =')'
            else:
                u[i] ='('
        answer += "".join(u)    
    
    return answer