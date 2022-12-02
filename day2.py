#! /usr/bin/python3

INPUT_FILE = "inputs/day2.txt"

# A,X = Rock
# B,Y = Paper
# C,Z = Scissors

ROCK = 1
PAPER = 2
SCISSORS = 3

ROCK_OTHER = 'A'
PAPER_OTHER = 'B'
SCISSORS_OTHER = 'C'

WIN = 6
DRAW =  3
LOSE = 0

def play(guide, rules):
    result = 0
    for round in guide:
        round_rule = rules[round[1]]
        result += round_rule['value'] + round_rule['result'][round[0]]
    return result


with open(INPUT_FILE) as f: 
    sguide = [ l.replace('\n', '').split(' ') for l in f.readlines() ]

rules_part1 = {
            'X': { 'value': ROCK, 'result': { SCISSORS_OTHER: WIN, ROCK_OTHER: DRAW, PAPER_OTHER: LOSE } },
            'Y': { 'value': PAPER, 'result': { ROCK_OTHER: WIN, PAPER_OTHER: DRAW, SCISSORS_OTHER: LOSE } },
            'Z': { 'value': SCISSORS, 'result': { PAPER_OTHER: WIN, SCISSORS_OTHER: DRAW, ROCK_OTHER: LOSE } }
        }

print(play(sguide, rules_part1))

rules_part2 = {
        'X': { 'value': LOSE, 'result': { ROCK_OTHER: SCISSORS, PAPER_OTHER: ROCK, SCISSORS_OTHER: PAPER } },
        'Y': { 'value': DRAW, 'result': { ROCK_OTHER: ROCK, PAPER_OTHER: PAPER, SCISSORS_OTHER: SCISSORS } },
        'Z': { 'value': WIN, 'result': { ROCK_OTHER: PAPER, PAPER_OTHER: SCISSORS, SCISSORS_OTHER: ROCK } },
        }
print(play(sguide, rules_part2))
