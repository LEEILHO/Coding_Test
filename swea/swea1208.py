for tc in range(1,11):
    dumps = int(input())
    width = list(map(int, input().split()))
    for _ in range(dumps):
        max_height = max(width)
        min_height = min(width)
        if max_height-min_height >=1:
            width[width.index(max_height)] -=1
            width[width.index(min_height)] +=1
        else:
            break
    print("#{} {}".format(tc,max(width)-min(width)))
             