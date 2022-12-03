def priority(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96

with open('input') as file:
    lines = file.read().strip().split('\n')
    # Part 1 
    score1 = 0
    for line in lines:
        first = line[:len(line)//2]
        second = line[len(line)//2:]
        for char in first:
            if char in second:
                score1 += priority(char)
                break
    print(score1)

    # Part 2
    score2 = 0
    i = 0
    while i < len(lines):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                score2 += priority(c)
                break
        i += 3
    print(score2)
