with open('input') as f:
    lines = f.read().strip().splitlines()

pairs1 = 0
pairs2 = 0
for line in lines:
    first, second = line.split(',')
    first_range = list(map(int, first.split('-')))
    second_range = list(map(int, second.split('-')))

    # Part 1 
    condition1 = first_range[0] <= second_range[0] and first_range[1] >= second_range[1]
    condition2 = first_range[0] >= second_range[0] and first_range[1] <= second_range[1]

    if condition1 or condition2:
        pairs1 += 1

    # Part 2
    condition3 = len(set(range(first_range[0], first_range[1] + 1)) & set(range(second_range[0], second_range[1] + 1))) > 0
                         
    if condition3:
        pairs2 += 1

    print(pairs1, pairs2 )
