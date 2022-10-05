# 스택 예제
stack = []
#삽입5 삽입 2 삽입 3 삽입 7 삭제 삽입1 삽입4 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
print(stack.pop())
print(stack)
print(stack[::-1])