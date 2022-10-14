""" 자물쇠와 열쇠
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견
문을 열려고 보니 특이한 형태의 자물쇠로 잠겨 있었다.
자물쇠는 격자 한칸의 크기가 1인 N x N 크기의 격자 형태이고 특이한 모양의 열쇠는 MxM 정사각 형태
자물쇠는 홈이 파여있고 열쇠또한 홈과 돌기 부분존재
열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분과 딱 맞게 채우면 자물쇠가 열림
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는데 영향을 주지 않지만 
자물쇠 영역내에서는 열쇠의 돌기 부분과 자물쇠의 홈부분이 정확히 일치 해야하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안되고 
자물쇠의 돌기과 열쇠의 돌기가 만나면 안된다. 모든 홈을 채워야 열림 
key = MxM 크기 이차원 배열
lock은 nxn 크기 2차원 배열
m은 항상 n이하
0은 홈부분 1은 돌기 부분
"""
#자물쇠 90도 회전
def rotate_key(key):
    n = len(key)
    m - len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j]
    return result

# 자물쇠의 중앙 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) //3
    for i in range(lock_length,lock_length *2):
        for j in range(lock_length,lock_length *2):
            if new_lock[i][j] == 0:
                return False
    return True


def solution(key,lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_key(key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                
                if check(new_lock) == True:
                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
                
    return False

