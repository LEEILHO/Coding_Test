# 퍼펙트 셔플
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    if N %2==0:
        left_cards = cards[0:N//2]
        right_cards = cards[N//2:N]
    else:
        left_cards = cards[0:N//2+1]
        right_cards = cards[N//2+1:N]
        
    print(left_cards)
    print(right_cards)
    result = []
    for i in range(len(right_cards)):
        result.append(left_cards[i])
        result.append(right_cards[i])
    if N %2 ==1:
        result.append(left_cards[-1])
    result = " ".join(result)
    print(f"#{tc} {result}")
        