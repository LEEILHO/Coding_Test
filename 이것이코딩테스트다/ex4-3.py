"""왕실의 나이트
체스판과 같은 8x8 좌표 평면 특정한 한칸에 나이트가 서있다. L자 형태로 이동가능함 밖으로는 못나감
이동 1. 수평 두 칸 이동 수직 한 칸 이동
이동 2. 수직 2칸 수평 1칸
첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표 두문자로 구성된 문자열 a1
"""
location= input()

col = int(location[1])
row = int(ord(location[0])) -int(ord('a')) +1 #아스키 코드 이용하여 a -> 1로 변환
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
result =0
for step in steps:
    next_col = col + step[0]
    next_row = row + step[1]
    if 1<=next_col <= 8 and 1<=next_row <= 8:
        result +=1
print(result) 
