notes = open('input_d11.txt').read().splitlines()
monkeys = {}


def parseItems(items):
    items = items.split(' ')
    itemList = []
    for i in items[4:]:
        if i[-1] == ',':
            itemList.append(int(i[:-1]))
        else:
            itemList.append(int(i))
    return itemList

def parseOperation(operation):
    operation = [operation.split(' ')[-2], operation.split(' ')[-1]]
    if operation[1] != 'old':
        operation[1] = int(operation[1])
    return operation

def parseTest(test):
    num = int(test.split(' ')[-1])
    return num

i = 0
D = 1
while i < len(notes):
    if notes[i].split(' ')[0] == 'Monkey':
        monkey = int(notes[i].split(' ')[1][:-1])
        monkeys[monkey] = {}
        i += 1
        items = parseItems(notes[i])
        i += 1
        operation = parseOperation(notes[i])
        i += 1
        test = parseTest(notes[i])
        D *= test
        i += 1
        true = parseTest(notes[i])
        i += 1
        false = parseTest(notes[i])
        i += 1
        monkeys[monkey]['items'] = items
        monkeys[monkey]['operation'] = operation
        monkeys[monkey]['test'] = test
        monkeys[monkey][True] = true
        monkeys[monkey][False] = false
    i += 1


def executeOperation(operation, item):
    if operation[1] == 'old':
        val = item
    else:
        val = operation[1]
    if operation[0] == '+':
        worryLevel = val + item
    elif operation[0] == '*':
        worryLevel = val * item
    return worryLevel

def monkeyBusiness(iterations):
    inspected = {}
    for i in range(iterations):
        for monkey in sorted(monkeys):
            if monkey not in inspected:
                inspected[monkey] = 0
            while monkeys[monkey]['items']:
                inspected[monkey] += 1
                worryLevel = monkeys[monkey]['items'].pop()
                worryLevel = executeOperation(monkeys[monkey]['operation'], worryLevel)
                # Uncomment for Part 1
                #worryLevel = int(worryLevel/3)
                worryLevel %= D
                result = worryLevel % monkeys[monkey]['test'] == 0
                passTo = monkeys[monkey][result]
                monkeys[passTo]['items'].append(worryLevel)
    
    
    topInspected = sorted(((v,k) for k,v in inspected.items()), reverse=True)
    print(topInspected)
    return topInspected[0][0] * topInspected[1][0]

# Part 1
#print(monkeyBusiness(20))
# Part 2
print(monkeyBusiness(10000))
