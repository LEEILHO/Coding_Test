import sys
from collections import Counter
N = int(input())
nums =[]
for _ in range(N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
means = round(sum(nums)/N)
median = nums[N//2]
modes = Counter(nums).most_common()
if len(modes)>1:
    if modes[0][1] == modes[1][1]:
        mode = modes[1][0]
    else:
        mode = modes[0][0]
else:
    mode = modes[0][0]
ranges = nums[-1] -nums[0]
print(means)
print(median)
print(mode)
print(ranges) 
    