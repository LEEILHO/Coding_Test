#순차 탐색 코드

def sequential_search(n,target,array):
    
    for i in range(n):
        if array[i] == target:
            return i+1
        
        
        
print("생성할 원소 개수를 입력한 다음 한 칸 뛰고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])

target = input_data[1]

array = input().split()
print(sequential_search(n, target,array))