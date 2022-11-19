T = int(input())
for tc in range(1,T+1):
    P,Q,R,S,W = map(int, input().split())
    A = W * P
    if W>R:
        B = Q + (W-R) * S
    else:
        B = Q
    print(f"#{tc} {min(A,B)}")