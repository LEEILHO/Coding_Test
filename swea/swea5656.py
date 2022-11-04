# 벽돌 꺠기
#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def deepcopy(graph):
    new_graph =[]
    for y in range(len(graph)):
        temp =[]
        for x in range(len(graph[y])):
            temp.append(graph[y][x])
        new_graph.append(temp)
    return new_graph
def erase_block(y,x,cur_block):
    q = deque()
    q.append((y,x,cur_block[y][x]))
    cur_block[y][x] =0
    erased_block = 1
    while q:
        now_y,now_x,now_power = q.popleft()
        for p in range(1,now_power):
            for d in range(4):
                ny,nx = now_y + p *dy[d], now_x + p * dx[d]
                if 0<= ny < H and 0 <=nx < W and cur_block[ny][nx] != 0:
                    if cur_block[ny][nx] !=1:
                        q.append((ny,nx,cur_block[ny][nx]))
                    erased_block +=1
                    cur_block[ny][nx] =0
    
    return erased_block

def sort_block(cur_block):
    for x in range(W):
        cur_w_block = []
        for y in range(H-1,-1,-1):
            if cur_block[y][x] !=0:
                cur_w_block.append(cur_block[y][x])
                cur_block[y][x] =0
        for h in range(len(cur_w_block)):
            cur_block[H-1-h][x] = cur_w_block[h]  

def dfs(result,k, block):
    global max_result
    if k ==N:
        if max_result < result:
            max_result = result
        return 
    for w in range(W):
        cur_block = deepcopy(block)
        cur_h = 0
        while cur_h < H and not cur_block[cur_h][w]:
            cur_h +=1
        
        num_erase =0
        if cur_h < H:
            num_erase = erase_block(cur_h, w, cur_block)
            sort_block(cur_block)
        dfs(result + num_erase,k+1,cur_block)


T = int(input())
for tc in range(1,T+1):  
    N, W,H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    num_all_block =0
    for y in range(H):
        for x in range(W):
            if graph[y][x] !=0:
                num_all_block +=1
    max_result=0
    dfs(0,0,graph)
    print("#{} {}".format(tc,num_all_block-max_result))

