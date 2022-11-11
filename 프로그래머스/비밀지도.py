def to_binary(n,num):
    ans = ""
    while (num > 0):
        div, mod = num //2, num%2
        num = div
        ans += str(mod)
    ans = ans[::-1]
    ans = ans.zfill(n)
    return ans
    


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans1 = to_binary(n,arr1[i])
        ans2 = to_binary(n,arr2[i])
        result =""
        for j in range(n):
            if ans1[j]=="1" or ans2[j]=="1":
                result +="#"
            else:
                result += " "
        answer.append(result)
        
    
    return answer