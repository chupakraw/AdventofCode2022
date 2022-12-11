"""
Part 1:
To begin, find all of the directories with a total size of at most 100000, 
then calculate the sum of their total sizes. In the example above, 
these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). 
(As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. 
What is the sum of the total sizes of those directories?

Part 2:
The total disk space available to the filesystem is 70000000. 
To run the update, you need unused space of at least 30000000. 
You need to find a directory you can delete that will free up 
enough space to run the update.

Find the smallest directory that, if deleted, would free up 
enough space on the filesystem to run the update. 
What is the total size of that directory?
"""

commands = open('input_d7.txt').read().splitlines()

def get_size(commands):
    # Part 1
    directory = {}
    path = []
    pn = ''
    under = set()

    for command in commands:
        command = command.split()
        if '$' in set(command) and 'cd' in set(command):
            if command[-1] != '..':
                # Need to keep track of directory path
                # and a unique name for each directory
                path.append(command[-1])
                pn += command[-1]
                if pn not in directory:
                    directory[pn] = {'size': 0, 'files': set()}
            else:
                last = path.pop()
                pn = pn[:-len(last)]
        elif '$' not in set(command) and 'dir' not in set(command):
            # Check if file size was already added
            # If not, rebuild unique directory name
            # and add file size to all directories in path
            if command[-1] not in directory[pn]['files']:
                temp = ''
                for i in path:
                    temp += i
                    directory[temp]['size'] += int(command[0])
                    if directory[temp]['size'] <= 100000:
                        under.add(temp)
                    if directory[temp]['size'] > 100000 and temp in under:
                        under.remove(temp)
                directory[pn]['files'].add(command[-1])

    # Part 2
    spaceNeeded = 30000000 - (70000000 - directory['/']['size'])
    ans = 70000000
    
    for i in directory:
        if directory[i]['size'] >= spaceNeeded:
            ans = min(ans, directory[i]['size'])

    # Part 1, Part 2
    return sum([directory[i]['size'] for i in under]), ans

print(get_size(commands))
