"""
Part 1:
To fix the communication system, you need to add a subroutine 
to the device that detects a start-of-packet marker in the datastream. 
In the protocol being used by the Elves, the start of a packet is indicated 
by a sequence of four characters that are all different.
Here are a few more examples:

    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

How many characters need to be processed before the first 
start-of-packet marker is detected?

Part 2:
A start-of-message marker is just like a start-of-packet marker, 
except it consists of 14 distinct characters rather than 4.

How many characters need to be processed before the first 
start-of-message marker is detected?
"""

datastream = open('input_d6.txt').read()

def findMarkerP1(datastream):
    c = 0
    char = {}

    while c < len(datastream):
        if datastream[c] not in char:
            char[datastream[c]] = c
            c += 1
        else:
            c = char[datastream[c]] + 1
            char = {}
        if len(char) == 4:
            return c

def findMarkerP2(datastream):
    c = 0
    char = {}

    while c < len(datastream):
        if datastream[c] not in char:
            char[datastream[c]] = c
            c += 1
        else:
            c = char[datastream[c]] + 1
            char = {}
        if len(char) == 14:
            return c

print(findMarkerP1(datastream))
print(findMarkerP2(datastream))
