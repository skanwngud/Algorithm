def solution(n, start, end, roads, traps):
    
    st = start
    time = 0
    road = roads
    
    for num2 in range(5):
        
        for index,road in enumerate(roads):
            
            if  st in traps:
                if st in road[:2] :
                    road[index]=[road[1], road[0], road[2]]
                else : road[index] = road
            else : road[index] = road
            
        max = 0
        time = 0
        
        for num in road:
            if num[0] == st:
                if num[1] >= max:
                    max = num[1]
                    time = num[2]

        st = max
        time += time
        
        if st == end:
            break
            
    return time