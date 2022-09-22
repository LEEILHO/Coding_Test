# swea13547 팔씨름
T = int(input())

for test_case in range(1, T + 1):
    arr = list(input())
    count = arr.count('o')
    if ((15-len(arr)) >= (8-count)): # 남은 경기가 앞으로 이겨야할 경기수보다 클 때 
        result = "YES"
    else:
        result = "NO"
    print("#{} {}".format(test_case,result))