#문자열의 거울상
T = int(input())
for tc in range(1,T+1):
    s = input()
    result = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] =="b":
            result = result + "".join("d")
        elif s[i] == "d":
            result = result + "".join("b")
        elif s[i] =="q":
            result = result + "".join("p")
        elif s[i] =="p":
            result = result + "".join("q")
    print(f"#{tc} {result}")