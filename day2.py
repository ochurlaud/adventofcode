#!/usr/bin/python3

print("## AdventOfCode 2022: day2")

INPUT_FILE = "inputs/day2.txt"

EXAMPLE = """A Y
B X
C Z"""

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
    rawdata = f.read()

#rawdata = EXAMPLE

sguide = [ l.split(' ') for l in rawdata.splitlines() ]

rules_part1 = {
            'X': { 'value': ROCK, 'result': { SCISSORS_OTHER: WIN, ROCK_OTHER: DRAW, PAPER_OTHER: LOSE } },
            'Y': { 'value': PAPER, 'result': { ROCK_OTHER: WIN, PAPER_OTHER: DRAW, SCISSORS_OTHER: LOSE } },
            'Z': { 'value': SCISSORS, 'result': { PAPER_OTHER: WIN, SCISSORS_OTHER: DRAW, ROCK_OTHER: LOSE } }
        }
print("Part 1: ", play(sguide, rules_part1))

rules_part2 = {
        'X': { 'value': LOSE, 'result': { ROCK_OTHER: SCISSORS, PAPER_OTHER: ROCK, SCISSORS_OTHER: PAPER } },
        'Y': { 'value': DRAW, 'result': { ROCK_OTHER: ROCK, PAPER_OTHER: PAPER, SCISSORS_OTHER: SCISSORS } },
        'Z': { 'value': WIN, 'result': { ROCK_OTHER: PAPER, PAPER_OTHER: SCISSORS, SCISSORS_OTHER: ROCK } },
        }
print("Part 2: ", play(sguide, rules_part2))
