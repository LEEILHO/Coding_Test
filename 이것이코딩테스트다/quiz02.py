""" 곱하기 혹은 더하기 
0부터 9로만 이루어진 문자열 s가 주어졌을때 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
단, +보다 x를 먼저 계산하는 일반적인 방식 과는 달리 모든 연산은 왼쪽에서부터 순서대로 이루어진다.
"""
s = input()
result = int(s[0])
for i in range(1,len(s)):
    #결과가 0혹은 1이거나 추가로 연산에 쓰일 숫자가 0혹은 1이면 +연산 수행
    if result ==0 or result ==1 or int(s[i]) ==0 or int(s[i] ==1):
        result +=int(s[i])
    #그 이외에는 X연산 수행
    else:
        result *= int(s[i])
print(result) 
