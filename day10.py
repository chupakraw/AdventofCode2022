instructions = open('input_d10.txt').read().splitlines()


# Part 1 ------------------------------------------------------------------------------

def checkCycle(cycle, cycleSum, signalStrengthSum):
    strengthCycles = {20,60,100,140,180,220}
    if cycle in strengthCycles:
        signalStrengthSum += (cycle * cycleSum)
    return signalStrengthSum

def signalStrength(instructions):
    cycles = []
    val = 1
    cycleSum = 1
    signalStrengthSum = 0

    for i in instructions:
        cycles.append(0)
        signalStrengthSum = checkCycle(len(cycles),cycleSum,signalStrengthSum)
        if i.split(' ')[0] == 'addx':
            val = int(i.split(' ')[1])
            cycles.append(val)
            signalStrengthSum = checkCycle(len(cycles),cycleSum,signalStrengthSum)
            cycleSum += val
    
    return signalStrengthSum


# Part 2 ------------------------------------------------------------------------------


def checkPixel(cycleSum,crt,row):
    sprite = {cycleSum-1,cycleSum,cycleSum+1}
    if len(crt[row]) in sprite:
        crt[row].append('#')
    else:
        crt[row].append('.')
    if len(crt[row]) == 40:
        crt.append([])
        row += 1
    return crt, row

def printSignal(instructions):
    crt = [[]]
    row = 0
    val = 1
    cycleSum = 1

    for i in instructions:
        crt, row = checkPixel(cycleSum,crt,row)
        if i.split(' ')[0] == 'addx':
            crt, row = checkPixel(cycleSum,crt,row)
            val = int(i.split(' ')[1])
            cycleSum += val
    
    return crt

    

print(signalStrength(instructions))
crt = printSignal(instructions)
for row in crt:
    print(row)
        