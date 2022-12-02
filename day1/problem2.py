with open('input') as file:
    totals = []
    elfs = file.read().strip().split('\n\n')
    for elf in elfs:
        lines = elf.split('\n')
        elfsum = sum(list(map(lambda x: int(x), lines)))
        
        totals.append(elfsum)

    print("Part 1: " + str(max(totals)))
    print("Part 2: " + str(sum(sorted(totals)[-3:])))
