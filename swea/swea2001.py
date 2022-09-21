# swea2001 파리 퇴치
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #n*n 행렬 
    max_die = 0
    for i in range(N-M+1):
        for j in range(N-M+1): #이중배열 순회하면서
            die = 0
            for x in range(i,i+M):
                for y in range(j, j+M):
                    die += arr[x][y] #죽는 파리수 더하기
            if die > max_die:
                max_die = die
    print("#{} {}".format(test_case,max_die))

