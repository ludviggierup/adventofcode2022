with open('input') as f:
    lines = f.read().strip().split('\n') 

G = []
for line in lines: 
    G.append(line)

R = len(lines[0])
C = len(lines)

DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
p1 = 0

for r in range(R):
    for c in range(C):
        visible = False
        for (dr, dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if G[rr][cc] >= G[r][c]:
                    ok = False
            if ok:
                visible = True
        if visible:
            p1 += 1
print(p1)

# Part 2
best = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr, dc) in DIR:
            rr = r
            cc = c
            steps = 0
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                steps += 1
                if G[rr][cc] >= G[r][c]:
                    break
            score *= steps
        if score > best:
            best = score
print(best)
