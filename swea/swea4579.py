#세상의 모든 펠린드롬
T = int(input())
for tc in range(1, T+1):
    s = input()
    reverse_s = s[::-1]
    for i in range(len(s)):
        if s[i] != reverse_s[i]:
            if s[i] != '*' and reverse_s[i] !='*':
                result = "Not exist"
                break
            else:
                result ="Exist"
                break
        else:
            result =  "Exist"
    print(f"#{tc} {result}")
        
        
