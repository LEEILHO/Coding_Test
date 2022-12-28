N = int(input())
arrs = list(map(int, input().split()))
new_arrs = list(sorted(set(arrs)))
dic = {}
for i in range(len(new_arrs)):
    dic[new_arrs[i]] = i
for i in arrs:
    print(dic[i], end =" ")
print()