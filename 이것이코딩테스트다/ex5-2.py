# 큐
from collections import deque
#삽입5 삽입 2 삽입 3 삽입 7 삭제 삽입1 삽입4 삭제
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #들어온 순서 대로 출력
queue.reverse()
print(queue) #나중에 들어온 순서
