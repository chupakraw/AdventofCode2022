"""
Part 1:
First, determine whether there is enough tree cover here to 
keep a tree house hidden. To do this, you need to count the 
number of trees that are visible from outside the grid when 
looking directly along a row or column.
Each tree is represented as a single digit whose value is its height, 
where 0 is the shortest and 9 is the tallest.
A tree is visible if all of the other trees between it and an edge of the 
grid are shorter than it. Only consider trees in the same row or 
column; that is, only look up, down, left, or right from any 
given tree.
Consider your map; how many trees are visible from outside 
the grid?

Part 2:
To measure the viewing distance from a given tree, look up, down, 
left, and right from that tree; stop if you reach an edge or at the 
first tree that is the same height or taller than the tree under consideration. 
(If a tree is right on the edge, at least one of its viewing distances will be zero.)
A tree's scenic score is found by multiplying together its viewing distance in each 
of the four directions.

Consider each tree on your map. 
What is the highest scenic score possible for any tree?

"""

grid = [list(line) for line in open('input_d8.txt').read().splitlines()]

def visibleTrees(grid):
    visibleTrees = (len(grid) * 2) + (len(grid[0]) * 2) - 4
    highestScore = 0
    
    for row in range(1,len(grid)-1):
        for col in range(1,len(grid[0])-1):
            tree = int(grid[row][col])
            if tree == 0:
                continue
            left = right = top = bottom = False
            leftScore = rightScore = topScore = bottomScore = 0
            for i in range(col-1,-1,-1):
                leftScore += 1
                if int(grid[row][i]) >= tree:
                    left = True
                    break
            for i in range(col+1,len(grid[0])):
                rightScore += 1
                if int(grid[row][i]) >= tree:
                    right = True
                    break
            for i in range(row-1,-1,-1):
                topScore += 1
                if int(grid[i][col]) >= tree:
                    top = True
                    break
            for i in range(row+1,len(grid)):
                bottomScore += 1
                if int(grid[i][col]) >= tree:
                    bottom = True
                    break
            highestScore = max(leftScore * rightScore * topScore * bottomScore, highestScore)
            if left and right and top and bottom:
                continue
            else:
                visibleTrees += 1
                
    return visibleTrees, highestScore

p1, p2 = visibleTrees(grid)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')