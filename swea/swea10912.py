#외로운 문자
T =int(input())
for tc in range(1,T+1):
    s = input()
    result =[]
    for i in range(len(s)):
        if s[i] not in result:
            result.append(s[i])
        else:
            result.remove(s[i])
    result.sort()
    if result:
        ans =""
        for i in result:
            ans+=i
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} Good")