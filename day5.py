"""
Part1:
The Elves just need to know which crate 
will end up on top of each stack;

After the rearrangement procedure completes, 
what crate ends up on top of each stack?
*** Crane can only move one crate at a time!!!

Part 2:
Crane can move multiple crates at a time.

"""
import copy

s, moves = open('input_d5.txt').read().split(' 1   2   3   4   5   6   7   8   9 ')
s = s.splitlines()
moves = moves.splitlines()[2:]

stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

for i in range(len(s)-1,-1,-1):
    stack = s[i].split(' ')
    count = 0
    stackNum = 1
    for j in range(len(stack)):
        if stack[j] == '':
            count += 1
            if count == 4:
                count = 0
                stackNum += 1
            continue
        else:
            stacks[stackNum].append(stack[j][1:len(stack[j])-1])
            stackNum += 1

stacks1 = copy.deepcopy(stacks)
stacks2 = copy.deepcopy(stacks)

def operateCraneP1(stacks1, moves):
    for move in moves:
        x = move.split(' ')
        crates = int(x[1])
        fromStack = int(x[3])
        toStack = int(x[5])
        for i in range(crates):
            stacks1[toStack].append(stacks1[fromStack].pop())
    
    ans = ''
    for i in range(1,len(stacks1)+1):
        if len(stacks1[i]) > 0:
            ans += stacks1[i][-1]
    
    return ans

def operateCraneP2(stacks2, moves):
    for move in moves:
        x = move.split(' ')
        crates = int(x[1])
        fromStack = int(x[3])
        toStack = int(x[5])
        stacks2[toStack] += stacks2[fromStack][-crates:]
        stacks2[fromStack] = stacks2[fromStack][:-crates]
    
    ans = ''
    for i in range(1,len(stacks2)+1):
        if len(stacks2[i]) > 0:
            ans += stacks2[i][-1]
    
    return ans

print(operateCraneP1(stacks1, moves))
print(operateCraneP2(stacks2, moves))

