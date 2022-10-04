""" 숫자 카드 게임 (가장 높은 숫자카드 뽑기)
 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다 N은 행의개수 M은 열이 개수 
 먼저 뽑고자 하는 카드가 포함되어 있는 행을 택한다.
 그다음 선택된 행에 포함된 카드들중 낮은 카드를 뽑아야한다
 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 낮은 카드를 뽑을 것을 고려햐어 최종적으로 가장 높은 숫자 뽑도록
 첫번째 줄 행의 개수 N 열의 개수 M
둘쨰 줄 부터 카드에 적힌 숫자 
"""
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for row in range(n):
    min_value = min(arr[row])
    result = max(result, min_value)
print(result)
        


