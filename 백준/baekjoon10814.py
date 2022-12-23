import sys
N = int(input())
joins = []
for i in range(N):
    age,name = sys.stdin.readline().rstrip().split()
    joins.append((int(age),name,i))
joins = sorted(joins, key = lambda x: (x[0],x[2]))
for info in joins:
    print(info[0],info[1])