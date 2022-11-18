# T = int(input())
# def swap(idx):
#     max_idx = idx
#     for i in range(idx,len(nums)):
#         if nums[i] >=nums[max_idx]:
#             max_idx = i
#     nums[idx],nums[max_idx] = nums[max_idx],nums[idx]

# #중복 없으면 True 반환
# def duplicate_check(nums):
#     if len(nums) == len(set(nums)):
#         return True
#     else:
#         return False
        
    
    
    
# for tc in range(1,T+1):
#     num,n = map(int,input().split())
#     nums = list(str(num))
#     max_num = sorted(nums,reverse=True)
#     cnt =0
#     duplicate = duplicate_check(nums)
    
#     result =""
#     for i in range(n):
#         if max_num == nums:
#             break
#         else:
#             for j in range(len(nums)):
                
                    
                
#                 # 중복이 존재하지 않을 때
#                 if max_num[j] !=nums[j]:
#                     #중복이 존재할 때:
#                     if duplicate and cnt+2 < n:
                        
                        
#                     else:
#                         print(nums)
#                         swap(j)
#                         print(nums)
#                         cnt+=1
#                         break
    
#     if(n == cnt):
#         result = "".join(nums)
#     else:
#         if((n-cnt)%2==0 or duplicate_check(nums)==False):
#             result = "".join(nums)
#         else:
#             nums[-1],nums[-2] = nums[-2],nums[-1]
#             result ="".join(nums)
#     # print(result)

def dfs(cnt, n):
    global answer
    if cnt == n:    # n만큼 바꿔줬다면
        temp = ''.join(board)   # 문자열로 바꿔주기
        if answer < temp:   # answer에 저장되어있는 값보다 크다면 갱신
            answer = temp
        return
 
    for i in range(len_b):
        for j in range(i+1, len_b): # 현재 자리(i)의 다음자리부터 비교
            board[i], board[j] = board[j], board[i] # 바꾸기
            temp = ''.join(board)               # 문자열로 바꿔
            if visited.get((temp, cnt), 1):     # 중복 아니라면
                visited[(temp, cnt)] = 0        # visited에 저장
                dfs(cnt+1, n)                 # 들어가기
            board[i], board[j] = board[j], board[i] # 원상복귀
 
 
for idx in range(1, int(input())+1):
    board, n = input().split()
    n = int(n)
    board = list(board)
    len_b = len(board)
    visited = {}            # 중복 방지 딕셔너리
    answer = '00000000'     # 정답 담는 변수 초기화
 
    dfs(0, n)
 
    print('#{} {}'.format(idx, answer))