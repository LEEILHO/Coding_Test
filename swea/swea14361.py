#swea14361 숫자가 같은 배수
import itertools
T = int(input())

for test_case in range(1, T + 1):

    result = "impossible"
    arr = list(map(int, input()))
    if len(arr) <=1: # 1자리의 정수이면 배수를 만들 수 없음
        result = "impossible"
    else:
        for value in itertools.permutations(arr,len(arr)): #순열을 돌면서
            arr2 = []
            for i in value: #제일처음에 오는 수가 0일경우 리스트에 값을 집어넣지 않음
                if (i !=0):
                    arr2.append(i)
                else:
                    if len(arr2) ==0:
                        continue
                    else:
                        arr2.append(i)
            if (len(arr2) != len(arr)):# 리스트의 길이가 다르면 성립X
                continue
            else:
                if (int("".join(map(str,value))) > int("".join(map(str,arr)))):
                    if (int("".join(map(str,value))) % int("".join(map(str,arr)))==0):
                        result = "possible"
                        break

    print("#{} {}".format(test_case,result))
                