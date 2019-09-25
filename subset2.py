T = int(input())

for _ in range(T):
    N, M, K = [ int(i) for i in input().strip().split(" ")]
    
    grid = {}
    x_coor = [0] * K
    y_coor = [0] * K
    
    for ele in range(K):
        x, y = [int(i) for i in input().strip().split(" ")]
        grid[str(x - 1) + " " + str(y - 1)] = 1
        
        x_coor[ele] = x - 1
        y_coor[ele] = y - 1
    c = 0
    if N == 1 or M == 1:
        print(4)
        continue
    
    for ele in range(K):
        
        #print("x_coor, y_coor", x_coor[ele], y_coor[ele])
        if x_coor[ele] == 0 or y_coor[ele] == 0 or x_coor[ele] == N - 1 or y_coor[ele] == M - 1:            
            if x_coor[ele] == 0 and y_coor[ele] != M - 1 and grid[str(x_coor[ele]) + " " + str(y_coor[ele])] == 1:
                #print("yeah1")
                c = c + 1
                f = True
                if x_coor[ele] == 0 and y_coor[ele] == 0:
                    f = False
                    c = c + 1
                if f and str(x_coor[ele]) + " " + str(y_coor[ele] - 1) not in grid:
                    c = c + 1
                if str(x_coor[ele]) + " " + str(y_coor[ele] + 1) not in grid:
                    c = c + 1
                if str(x_coor[ele] + 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
            elif y_coor[ele] == M - 1 and x_coor[ele] != N - 1 and grid[str(x_coor[ele]) + " " + str(y_coor[ele])] == 1:
                #print("yeah2")
                f = True
                c = c + 1
                if x_coor[ele] == 0 and y_coor[ele] ==  M - 1:
                    c = c + 1
                    f = False
                if f and str(x_coor[ele] - 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
                if str(x_coor[ele] + 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
                if str(x_coor[ele]) + " " + str(y_coor[ele] - 1) not in grid:
                    c = c + 1
            elif x_coor[ele] == N - 1 and y_coor[ele] != 0 and grid[str(x_coor[ele]) + " " + str(y_coor[ele])] == 1:
                #print("yeah3")
                c = c + 1
                f = True
                if x_coor[ele] == N - 1 and y_coor[ele] == M - 1:
                    c = c + 1
                    f = False
                if str(x_coor[ele]) + " " + str(y_coor[ele] - 1) not in grid:
                    c = c + 1
                if f and str(x_coor[ele]) + " " + str(y_coor[ele] + 1) not in grid:
                    c = c + 1
                if str(x_coor[ele] - 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
            elif y_coor[ele] == 0 and x_coor[ele] != 0 and grid[str(x_coor[ele]) + " " + str(y_coor[ele])] == 1:
                #print("yeah4")
                c = c + 1
                f = True
                if x_coor[ele] == N - 1 and y_coor[ele] == 0:
                    c = c + 1
                    f = False
                if str(x_coor[ele] - 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
                if f and str(x_coor[ele] + 1) + " " + str(y_coor[ele]) not in grid:
                    c = c + 1
                if str(x_coor[ele]) + " " + str(y_coor[ele] + 1) not in grid:
                    c = c + 1
            
            #print("c_boundary", c)
        
        else:
            #print("yeah5")
            if str(x_coor[ele] - 1) + " " + str(y_coor[ele]) not in grid:
                c = c + 1
            if str(x_coor[ele] + 1) + " " + str(y_coor[ele]) not in grid:
                c = c + 1
            if str(x_coor[ele]) + " " + str(y_coor[ele] - 1) not in grid:
                 c = c + 1
            if str(x_coor[ele]) + " " + str(y_coor[ele] + 1) not in grid:
                 c = c + 1
            #print("c_inside", c)
    print(c)