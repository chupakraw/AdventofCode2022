"""
Part 1:
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) 
that they say will be sure to help you win. "The first column is what your opponent is going to play: A 
for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, 
the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, 
and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won).

What would your total score be if everything goes exactly according to your strategy guide?
"""


strategy = open('input_d2.txt').read().splitlines()

def scorep1(strategy):
    score = 0
    scoring = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

    for match in strategy:
        score += scoring[match]
    
    return score


"""
Part 2:
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: X means you need to lose, 
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

Following the Elf's instructions for the second column, 
what would your total score be if everything goes exactly according to your strategy guide?
"""


def scorep2(strategy):
    score = 0
    scoring = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

    outcomes = {
        'X': {'A':'A Z', 'B':'B X', 'C':'C Y'},
        'Y': {'A':'A X', 'B':'B Y', 'C':'C Z'},
        'Z': {'A':'A Y', 'B':'B Z', 'C':'C X'},
    }

    for match in strategy:
        opponent, move = match.split(' ')
        score += scoring[outcomes[move][opponent]]
    
    return score


print(f'p1: {scorep1(strategy)}')
print(f'p2: {scorep2(strategy)}')