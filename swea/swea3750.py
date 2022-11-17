#swea3750 Digit sum
T = int(input())
results =[]
for tc in range(1,T+1):
    n = input()
    
    while len(n)>1:
        sum_total =0
        for num in n:
            sum_total += int(num)
        n = str(sum_total)
    results.append((tc,n))
for tc,result in results:
    print(f"#{tc} {result}")
    
#재귀
# def recursive(n):
#     sum_total=0
#     if len(n)>1:
#         for num in n:
#             sum_total += int(num)
#         return recursive(str(sum_total))
#     else:
#         return n
# T = int(input())
# results =[]
# for tc in range(1,T+1):
#     n = input()
#     results.append((tc,recursive(n))) 
# for tc,result in results:
#     print(f"#{tc} {result}")
    