"""
Part 1:
Space needs to be cleared before the last supplies can be unloaded 
from the ships, and so several Elves have been assigned the job of 
cleaning up sections of the camp. Every section has a unique ID number,
 and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments 
with each other, they've noticed that many of the assignments overlap. 
To try to quickly find overlaps and reduce duplicated effort, 
the Elves pair up and make a big list of the section assignments 
for each pair (your puzzle input).

In how many assignment pairs does one range fully contain the other?

Part 2:


"""

assignments = open('input_d4.txt').read().splitlines()

def countOverlapsp1(assignments):
    overlaps = 0
    
    for pairs in assignments:
        elf1, elf2 = pairs.split(',')
        l1, r1 = elf1.split('-')
        l2, r2 = elf2.split('-')
        l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
            overlaps += 1
    
    return overlaps


def countOverlapsp2(assignments):
    overlaps = 0
    
    for pairs in assignments:
        elf1, elf2 = pairs.split(',')
        l1, r1 = elf1.split('-')
        l2, r2 = elf2.split('-')
        l1, r1, l2, r2 = int(l1), int(r1), int(l2), int(r2)
        if (l1 <= l2 and r1 >= r2) or (l2 <= l1 and r2 >= r1):
            overlaps += 1
        elif (l1 < l2 and r1 >= l2) or (l2 < l1 and r2 >= l1):
            overlaps += 1
    
    return overlaps


print(countOverlapsp1(assignments))
print(countOverlapsp2(assignments))