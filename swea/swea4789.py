#성공적인 공연 기획
T = int(input())
for tc in range(1,T+1):
    S = input()
    people = 0
    result =0
    for i in range(len(S)):
        if int(S[i]) !=0:
            
            if people > i:
                people +=int(S[i])
            else:
                result += i - people
                people += (i - people) + int(S[i])
    print(f"#{tc} {result}")
            