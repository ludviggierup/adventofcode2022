with open('input') as file:
    topthree = [0, 0, 0]
    current = 0    
    for line in file.readlines():
        if line == '\n' or line == '':
            if current > topthree[0]:
                topthree[2] = topthree[1]
                topthree[1] = topthree[0]
                topthree[0] = current
                #topthree = [current] + topthree[1:]
            elif current > topthree[1]:
                topthree[2] = topthree[1]
                topthree[1] = current
            elif current > topthree[2]:
                topthree[2] = current
            current = 0
        else:
            current += int(line)
    print("Total: " + str(sum(topthree)))

