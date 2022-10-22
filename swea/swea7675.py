# 통역사 성경이
""" 
외국 대사는 총 N개의 문장을 말함
각 문장의 단어는 세가지 구두점 . ? ! 중 하나를 마지막에 포함
이름은 대문자 알파벳으로 시작하여 나머지는 소문자 알파벳인 단어들
N개의 문장을 받아 문장 별로 이름의 개수를 구하라
N개의 수를 공백 하나로 구분하여 출력, 각 수는 문장에 속한 이름의 개수
"""


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    paragraph = input().strip().replace('?','.').replace('!','.')
    sentences = paragraph.split('.')
    name =[]
    #문장 개수가 제일 마지막 문단의 구두점 이후에 하나 더생기는 거 기억!
    for sentence in sentences:
        name_cnt =0
        words = sentence.split()
        if sentence:
            for word in words:
                if len(word)>=2:
                    if word[0] == word[0].upper():
                        if word[1:len(word)] == word[1:len(word)].lower() and word[1:len(word)].isalpha()==True:
                            name_cnt +=1
            name.append(name_cnt)
    print("#{} {}".format(tc, ' '.join(map(str,name))))
                        
                    
                
