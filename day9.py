"""
Part 1:


"""
data = open('input_d9.txt').read().splitlines()
motions = []
for i in data:
    motions.append([i.split(' ')[0],int(i.split(' ')[1])])


def moveStraight(tail,head):
    if abs((tail[0]+1-head[0])) == 1 and tail[1] == head[1]:
        tail[0] += 1
        return tail
    elif abs((tail[0]-1)-head[0]) == 1 and tail[1] == head[1]:
        tail[0] -= 1
        return tail
    elif abs((tail[1]+1)-head[1]) == 1 and tail[0] == head[0]:
        tail[1] += 1
        return tail
    elif abs((tail[1]-1)-head[1]) == 1 and tail[0] == head[0]:
        tail[1] -= 1
        return tail


def moveDiagonal(tail,head):
    if abs((tail[0]+1)-head[0]) + abs((tail[1]+1)-head[1]) <= 2:
        tail[0] += 1
        tail[1] += 1
        return tail
    elif abs((tail[0]+1)-head[0]) + abs((tail[1]-1)-head[1]) <= 2:
        tail[0] += 1
        tail[1] -= 1
        return tail
    elif abs((tail[0]-1)-head[0]) + abs((tail[1]+1)-head[1]) <= 2:
        tail[0] -= 1
        tail[1] += 1
        return tail
    elif abs((tail[0]-1)-head[0]) + abs((tail[1]-1)-head[1]) <= 2:
        tail[0] -= 1
        tail[1] -= 1
        return tail


def moveTail(head,tail):
    if (abs(tail[0] - head[0]) == 2 and tail[1] == head[1]) or (abs(tail[1] - head[1]) == 2 and tail[0] == head[0]):
        tail = moveStraight(tail,head)
        return tail
    elif abs(tail[0] - head[0]) + abs(tail[1] - head[1]) > 2:
        tail = moveDiagonal(tail,head)
        return tail
    else:
        return tail


def tailPositionsP1(motions):
    head = [0,0]
    tail = [0,0]
    tailVisited = set()
    tailVisited.add(str(tail))
    moves = {
        'R': [0,1],
        'L': [0,-1],
        'U': [1,1],
        'D': [1,-1]
    }

    for i in motions:
        direction = moves[i[0]][0]
        step = moves[i[0]][1]
        for j in range(i[1]):
            head[direction] += step
            tail = moveTail(head,tail)
            if str(tail) not in tailVisited:
                tailVisited.add(str(tail))

    return len(tailVisited)


def tailPositionsP2(motions):
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tailVisited = set()
    tailVisited.add(str(rope[-1]))
    moves = {
        'R': [0,1],
        'L': [0,-1],
        'U': [1,1],
        'D': [1,-1]
    }

    for i in motions:
        direction = moves[i[0]][0]
        step = moves[i[0]][1]
        for j in range(i[1]):
            rope[0][direction] += step
            for k in range(len(rope)-1):
                rope[k+1] = moveTail(rope[k],rope[k+1])
            if str(rope[-1]) not in tailVisited:
                tailVisited.add(str(rope[-1]))

    return len(tailVisited)

print(tailPositionsP1(motions))
print(tailPositionsP2(motions))