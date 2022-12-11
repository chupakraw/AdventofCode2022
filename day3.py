"""
Part 1:
The list of items for each rucksack is given as characters all on a single line. 
A given rucksack always has the same number of items in each of its two compartments, 
so the first half of the characters represent items in the first compartment, 
while the second half of the characters represent items in the second compartment.

To help prioritize item rearrangement, every item type can be converted to a priority:

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

Find the item type that appears in both compartments of each rucksack. 
What is the sum of the priorities of those item types?

"""

import string

list = open('input_d3.txt').read().splitlines()

def prioritiesp1(list):
    sum_of_priorities = 0
    for rucksack in list:
        c1, c2 = set(rucksack[:int(len(rucksack)/2)]), set(rucksack[int(len(rucksack)/2):])
        item = c1.intersection(c2).pop()
        if item.isupper():
            priority = string.ascii_uppercase.index(item) + 27
        else:
            priority = string.ascii_lowercase.index(item) + 1
        sum_of_priorities += priority
    
    return sum_of_priorities


"""
Part 2:
Every set of three lines in your list corresponds to a single group, 
but each group can have a different badge item type.
Find the item type that corresponds to the badges of each three-Elf group. 
What is the sum of the priorities of those item types?
"""

def prioritiesp2(list):
    sum_of_priorities = 0
    for i in range(0,len(list),3):
        s1, s2, s3 = set(list[i]), set(list[i+1]), set(list[i+2])
        item = s1.intersection(s2)
        item = item.intersection(s3).pop()
        if item.isupper():
            priority = string.ascii_uppercase.index(item) + 27
        else:
            priority = string.ascii_lowercase.index(item) + 1
        sum_of_priorities += priority
    
    return sum_of_priorities



print(f'p1: {prioritiesp1(list)}')
print(f'p2: {prioritiesp2(list)}')





