T = int(input())

for test_case in range(1, T + 1):
    S = input()
    output = 0
    if  S == "MON":
        output= 6
    elif S =="TUE":
        output=5
    elif S =="WED":
        output=4
    elif S =="THU":
        output=3
    elif S=="FRI":
        output=2
    elif S =="SAT":
        output =1
    elif S =="SUN":
        output = 7
    print("#{} {}".format(test_case,output))
       


