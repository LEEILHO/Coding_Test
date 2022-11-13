#모음이 보이지 않는 사람
import re
T = int(input())
for tc in range(1,T+1):
    s = input()

    result = re.sub('a|e|i|o|u',"",s)
    print(f"#{tc} {result}")
# T = int(input())
# for tc in range(1,T+1):
#     s = input()
#     arr = ['a','e','i','o','u']
#     result =""
#     for i in s:
#         if i not in arr:
#             result +=i
#     print(f"#{tc} {result}")