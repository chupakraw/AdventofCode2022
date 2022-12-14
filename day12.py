#grid = [list(i) for i in open('test.txt').read().splitlines()]
grid = [list(i) for i in open('input_d12.txt').read().splitlines()]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'E':
            end = (i,j)
            grid[i][j] = 26
        elif grid[i][j] == 'S':
            start = (i,j)
            grid[i][j] = 1
        elif grid[i][j] == 1 or grid[i][j] == 26:
            continue
        else:
            grid[i][j] = ord((grid[i][j]).lower()) - 96


def climbP1(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) == start:
                queue = [start]
                visited = {}
                while queue:
                    cur = queue[0]
                    for k in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nex = tuple(map(sum, zip(k,cur)))
                        if 0 <= nex[0] < len(grid) and 0 <= nex[1] < len(grid[0]):
                            if grid[nex[0]][nex[1]] - grid[cur[0]][cur[1]] <= 1:
                                if nex not in visited:
                                    visited[nex] = cur
                                    queue.append(nex)
                    queue.pop(0)
    fr = end
    path = []
    while fr != start:
        path.append(fr)
        if fr in visited:
            fr = visited[fr]
    return len(path)


# Start from End and stop at first value of 1

def climbP2(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) == end:
                queue = [end]
                visited = {}
                while queue:
                    cur = queue[0]
                    for k in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nex = tuple(map(sum, zip(k,cur)))
                        if 0 <= nex[0] < len(grid) and 0 <= nex[1] < len(grid[0]):
                            if grid[cur[0]][cur[1]] - grid[nex[0]][nex[1]] <= 1:
                                if nex not in visited:
                                    visited[nex] = cur
                                    queue.append(nex)
                                if grid[nex[0]][nex[1]] == 1:
                                    start = nex
                                    fr = start
                                    path = []
                                    while fr != end:
                                        path.append(fr)
                                        if fr in visited:
                                            fr = visited[fr]
                                    return len(path)
                    queue.pop(0)

                


print(climbP1(grid))
print(climbP2(grid))

