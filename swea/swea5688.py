# 세젭곤을 찾아라
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cnt =1
    while(cnt**3< n):
        cnt+=1
    if cnt **3 ==n:
        print(f"#{tc} {cnt}")
    else:
        print(f"#{tc} -1")
 
#이진 탐색으로 풀어보기

# s,e = 1,n
# while s <=e:
#     m =(s+e)//2
#     if N==m **3:
#         ans = m
#         break
#     elif N <m**3:
#         e= m-1
#     else:
#         s= m+1