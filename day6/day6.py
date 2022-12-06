with open('input') as f:
    line = f.read()

last_three = []
for i, char in enumerate(line):
    if i < 13: # < 3 for part 1
        last_three.append(char)
        continue
    last_three.append(char)
    if len(last_three) == len(set(last_three)):
        print(i + 1)
        break
    last_three = last_three[1:]
