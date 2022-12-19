with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

# Part 1
dirs = {}
currentdir = ""
for i, line in enumerate(lines):
    split = line.split()
    if split[0] == '$':
        if split[1] == 'cd':
            if split[2] == '/':
                currentdir = '/'
            elif split[2] == '..':
                currentdir = '/'.join(currentdir.split('/')[:-1])
            else:
                if currentdir == '/':
                    currentdir += split[2]
                else:
                    currentdir += '/' + split[2]
    else:
        if currentdir in dirs:
            dirs[currentdir].append(line)
        else:
            dirs[currentdir] = [line]

dirsize = {}
for key in dirs.keys():
    dirsize[key] = 0

def calculate(currentdir):
    size = 0
    content = dirs[currentdir]
    for item in content:
        first, second = item.split()
        if (first.isdigit()):
            size += int(first)
        else:
            if currentdir == '/':
                size += calculate('/' + second)
            else:
                size += calculate(currentdir + '/' + second)
    dirsize[currentdir] = size
    return size

calculate('/')

thebigones = list(filter(lambda x: x[1] <= 100000 , dirsize.items()))
sumofbigones = sum(list(map(lambda x: x[1], thebigones)))
print(sumofbigones)

# Part 2
used_space = dirsize['/']
needed_space = 4e7
best = 1e9
for k, v in dirsize.items():
    if used_space - v < 4e7 and v < best:
        best = v
print(best)
