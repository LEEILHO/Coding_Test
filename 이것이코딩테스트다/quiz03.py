"""" 
문자열 뒤집기 
S는 0과 1로만 이루어져있는 문자열
모든 숫자를 전부 같게 만들려고 한다. 
S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
문자열 s가 주어졌을때 행동의 최소 횟수를 출력하시오.
"""
s = input()
cnt_zero = s.count('0')
cnt_one = s.count('1')
result =0
if cnt_zero > cnt_one: #0의 개수가 1보다 클 떄
    for i in range(len(s)-1):
        if s[i] =='1': #리스트에 있는 문자가 1일때
            if s[i+1] =='0': # #다음 문자가 0이면 result에 1 더함
                result +=1
else:
    for i in range(len(s)-1):
        if s[i] =='0':
            if s[i+1] =='1':
                result +=1

print(result)







