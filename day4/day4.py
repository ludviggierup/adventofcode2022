with open('input') as f:
    lines = f.read().strip().splitlines()

pairs1 = 0
pairs2 = 0
for line in lines:
    first, second = line.split(',')

    s1, e1 = first.split('-')
    s2, e2 = second.split('-')
    s1,e1,s2,e2 = [int(x) for x in [s1, e1, s2, e2]]

    if (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2):
        pairs1 += 1
    
    if not(e1 < s2 or e2 < s1): # not(not overlapping) 
        pairs2 += 1

print(pairs1, pairs2 )
