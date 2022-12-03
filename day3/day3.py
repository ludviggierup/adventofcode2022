def priority(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

def group(xs):
    return list(xs[i:i+3] for i in range(0, len(xs), 3))

with open('input') as file:
    lines = file.read().strip().split('\n')
    # Part 1 
    errors = []
    for line in lines:
        first = line[:len(line)//2]
        second = line[len(line)//2:]

        found = False
        for char in first:
            if found:
                continue
            if char in second:
                errors.append(char)
                found = True

    # Part 2
    badges = []
    for elfgroup in group(lines):
        print(group(lines))
        badge = list(set(elfgroup[0]) & set(elfgroup[1]) & set(elfgroup[2])).pop()
        badges.append(badge)

    part1 = sum(list(map(priority, errors)))
    print(part1)
    
    part2 = sum(list(map(priority, badges)))
    print(part2)
