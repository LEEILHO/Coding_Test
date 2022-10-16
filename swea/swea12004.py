#구구단1
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    result_list = []
    for i in range(1,10):
        for j in range(1,10):
            result_list.append(i*j)
    if n in result_list:
        print("#{} {}".format(test_case,"Yes"))
    else:
        print("#{} {}".format(test_case,"No"))