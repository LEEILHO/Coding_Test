# View
for tc in range(1,11):
    width = int(input())
    buildings = list(map(int,input().split()))
    light_building =0
    for building in range(len(buildings)):
        if buildings[building] ==0:
            continue
        else:
            now =buildings[building]
            left1 = buildings[building-1]
            left2 = buildings[building-2]
            right1= buildings[building+1]
            right2= buildings[building+2]
            
            if max(now,left1,left2,right1,right2) ==now:
                light_building+=now-max(left1,left2,right1,right2)
            else:
                continue
    print(f"#{tc} {light_building}")