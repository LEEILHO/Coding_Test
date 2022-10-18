# 알파벳 공부

T = int(input())
for tc in range(1,T+1):
    s = input()
    count =0
    ascii =97
    for i in s:
        if int(ord(i)) ==ascii:
             count +=1
             ascii +=1
        else:
            break
    print(f"#{tc} {count}")