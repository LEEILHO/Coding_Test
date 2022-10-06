"""두 배열의 원소 교체
동빈이 두 배열 A, B를 가짐 N개의 원소로 구성되어 있음 원소는 모두 자연수 
최대 K번의 바꿔치키 연산할 수 있음
바꿔치기 연산이란 배열 A에 있는 원소와 B에 있는 원소를 서로 바꾸는 것 동빈이는 최종 목표는 배열 A의 합이 최대가 되도록 하는 것.
첫번째 줄 N,K 가 공백으로 구분되어 입력
둘째 줄에 A의 원소가 공백으로 구분
B의 원소가 공백으로 구분"""
n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#k번 바꿔치키 ===> a를 정렬 낮은수부터 K개 b를 정렬하여 높은수 K개 바꾸기
# b의 최대값이 a의 최소값보다 작으면?? 바꾸지 않음 
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
    