#반반

T = int(input())
for test_case in range(1,T+1):
    s = input()
    result = []
    cnt1 =1
    cnt2 =1
    for i in s:
        if i not in result:
            result.append(i)
        else:
            if result.index(i) ==0:
                cnt1 +=1
            elif result.index(i) ==1:
                cnt2 +=1
    if cnt1==2 and cnt2 ==2:
        print("#{} {}".format(test_case,"Yes"))
    else:
         print("#{} {}".format(test_case,"No"))
        