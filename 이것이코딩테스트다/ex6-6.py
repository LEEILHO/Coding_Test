"""
성적이 낮은 순서로 학생 출력하기
N명의 학생 정보가 있다. 학생정보는 이름과 성적으로 구분된다. 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
첫째 줄 N 입력 1<= 100000
둘째줄 문자열 A와 정수 B가 공백으로 구분되어 출력
"""
n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))
    
array = sorted(array, key = lambda student: student[1])

for student in array:
    print(student[0], end = ' ')
