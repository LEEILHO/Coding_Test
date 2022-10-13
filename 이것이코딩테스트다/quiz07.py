""" 럭키 스트레이트
필살기인 럭키 스트레이트 기술이 있다. 매우 강력하여 특정조건을 만족 할때만 사용할 수 있다.
특정 조건이란 현재 캐리턱의 점수를 N이라고 할때 자릿수를 기준으로 N을 반으로 나누어 
왼쪽 부분의 자릿수 합과 오른쪽 자릿수의 합이 동일한 상황을 의미 정수가 주어지면 스트레이트를 사용할 수 있는 알려주는 프로그램을 작성하시오.
단, 점수 N의 자릿수는 학상 짝수 형태로만 주어진다.
사용할수 있다면 "LUCKY" 없으면 "READY" 출력
"""
n = int(input())
arr =list(str(n))
left =0
right =0
center = (len(arr)/2) -1
for i in range(len(arr)):
    if i <= center: 
        left += int(arr[i])
    else:
        right += int(arr[i])
if left ==right:
    print("LUCKY")
else:
    print("READY")