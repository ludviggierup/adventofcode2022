with open('input') as file:
    highest = 0
    current = 0
    for line in file.readlines():
        if line == '\n' or line == '':
            if current > highest:
                highest = current
            current = 0
        else:
            current += int(line)
    print("Highest: " + str(highest))
