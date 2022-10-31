""" 국영수
도현이네 반 학생의 국어, 영어, 수학 점수 주어진다.
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어점수가 증가 하는 순서로
3. 국어 점수와 영어점수가 같으면 수학점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
정렬하는 프로그램을 작성
첫째 줄 N
둘째 줄 국영수 점수 공백으로 구분하여 
점수는 1보다 크고 100이하
이름은 알파벳 대소문자로 이루어진 문자열"""
N = int(input())
result = []

for _ in range(N):    
    name,kor,eng,math= input().split()
    result.append((name,int(kor),int(eng),int(math)))
result = sorted(result, key = lambda x: (-x[1],x[2],-x[3] ,x[0] )  )

for name in result:
    print(name[0])
