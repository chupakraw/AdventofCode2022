# Parsing input by each line
# Converting sensor, beacon coordinates into complex numbers
def find_all(line):
    line = line[line.find('=')+1:]
    x = int(line[:line.find(',')])
    line = line[line.find('=')+1:]
    y = int(line[:line.find(':')])
    sensor = x + y*1j
    line = line[line.find('=')+1:]
    x = int(line[:line.find(',')])
    line = line[line.find('=')+1:]
    y = int(line)
    beacon = x + y*1j
    return [sensor, beacon]

#coor = list(map(find_all, open('test.txt').read().strip().splitlines()))
coor = list(map(find_all, open('input_d15.txt').read().strip().splitlines()))


def rangesAtY(y):
    ranges = []

    for s, b in coor:
        # Distance between signal and beacon
        distance = abs(int(s.real) - int(b.real)) + abs(int(s.imag) - int(b.imag))
        
        # signal y-coor + distance is the largest y-coor where a beacon cannot be
        # To find where beacons can't be at y, check if y is within this range
        if y <= int(s.imag) + distance:
            # Solve the absolute equation for x-coor range at y
            diff = distance - abs(int(s.imag) - y)
            xl = -1 * (diff - int(s.real))
            xr = -1 * (-diff - int(s.real))
            ranges.append((xl,xr))
    
    ranges.sort()
    combR = []
    for l, r in ranges:
        if not combR:
            combR.append([l,r])
            continue
        rl, rr = combR[-1]

        if l > rr + 1:
            combR.append([l,r])
            continue
        combR[-1][1] = max(rr, r)

    return combR


def noSignalatY(y):
    noBeacons = set()
    beaconAtY = set()
    ranges = rangesAtY(y)
    for l, r in ranges:
        for x in range(l, r+1):
            noBeacons.add(x)
    
    for s, b in coor:
        # Don't count if beacon at y
        if int(b.imag) == y:
            beaconAtY.add(int(b.real))
    
    return len(noBeacons - beaconAtY)

def distressSignal(y):
    for i in range(y+1):
        if i % 100000 == 0:
            print(i)
        freq = 0
        ranges = rangesAtY(i)
        for l, r in ranges:
            if freq < l:
                return (freq * 4000000 + i)
            freq = max(freq, r + 1)
            if freq > y:
                break


#print(noSignalatY(10))
print(noSignalatY(2000000))

#print(distressSignal(20))
print(distressSignal(4000000))


    