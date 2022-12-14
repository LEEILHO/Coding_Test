"""문자열 압축
데이터 처리 저눈가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부하고 있습니다. 
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더짧은
문자열로 표한하는 알고리즘을 공부 
"aabbcc" => 2a2b2c
이러한 방식은 반복되는 문자가 적을 경우 압축률이 낮음
단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법
ababcdabcd 2개 단위 => 2abcdabcd, 4개단위 => ab2abcd
압축할 문자열 s가 매개변수로 주어질 때 1개 이상 단위로 문자열을 잘라 압축하여 표현하는 문자열 중 가장 짧은 것의 길이를
return 하도록 solution 함수를 완성하시오.
"""
def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2 +1 ):
        compressed =""
        prev = s[0:step]
        count =1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count +=1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count=1
        compressed += str(count) + prev if count >= 2 else prev
        answer =min(answer,len(compressed))



    return answer

