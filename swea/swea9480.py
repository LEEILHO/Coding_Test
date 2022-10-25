#민정이와 광직이의 알파벳 공부
#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&problemLevel=2&problemLevel=3&contestProbId=AXAdrmW61ssDFAXq&categoryId=AXAdrmW61ssDFAXq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4&problemLevel=1%2C2%2C3&&&&&&&&&
def dfs(idx,used):
    global res
    if idx ==n:
        s=''
        for i in range(n):
            if used[i]:
                s+=words[i]
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) not in s:
                break
        else:
            res += 1
        return
    dfs(idx+1,used)
    used[idx] =1
    
    dfs(idx+1,used)
    used[idx] =0
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    words = [input() for _ in range(n)]
    res =0
    dfs(0,[0]*n)
    print(f'#{tc} {res}')
    