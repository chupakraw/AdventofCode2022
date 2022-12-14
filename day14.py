"""
coor = []
xmin, xmax, ymax = float("inf"), 0, 0
for line in open('test.txt').read().splitlines():
    huh = []
    for p in line.split(' -> '):
        a, b = map(eval, p.split(','))
        xmin, xmax, ymax = min(xmin,a), max(xmax, a), max(ymax, b)
        huh.append((a,b))
    coor.append(huh)
print(coor,xmin, xmax, ymax)

cave = [['.' for _ in range(0, ymax+1)] for _ in range(0,xmax-xmin+1)]

for line in coor:
    i = 0
    x1,y1 = line[i]
    while i < len(line) - 1:
        if x - 

for i in cave:
    print(i)
"""

# Code from hyper-neutrino:
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day14p2.py


blocked = set()
abyss = 0

for line in open('input_d14.txt'):
    x = [list(map(int, p.split(','))) for p in line.strip().split(' -> ')]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                blocked.add(x + y * 1j)
                abyss = max(abyss, y + 1)


t = 0

while 500 not in blocked:
    s = 500
    while True:
        if s.imag >= abyss:
            break
        if s + 1j not in blocked:
            s += 1j
            continue
        if s + 1j - 1 not in blocked:
            s += 1j - 1
            continue
        if s + 1j + 1 not in blocked:
            s += 1j + 1
            continue
        break
    blocked.add(s)
    t += 1

print(t)

