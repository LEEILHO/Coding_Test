# 14555 공과 잡초


T = int(input())

for test_case in range(1, T + 1):
    S = input()
    print("#{0} {1}".format(test_case,S.count('(')+S.count(')')-S.count('()')))#'(의 개수 +)의 개수 ()개수를 뺴면 공의 최소가 나온다

