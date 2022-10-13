""" 문자열 재정렬
알파벳 대문자와 숫자 0~9로만 구성된 문자열이 입력으로 주어진다.
모든 알파벳을 오름차순으로 정렬하여 이어서 출력, 그 뒤 모든 숫자를 더한값을 이어서 출력한다.
요구하는 정답 출력 """
s = input()
string_result =[]
int_result =[]
check_integer = ['0','1','2','3','4','5','6','7','8','9']
for i in s:
    if i in check_integer:
        int_result.append(int(i))
    else:
        string_result.append(i) 
string_result.sort()
for i in string_result:
    print(i,end='')
print(sum(int_result))
