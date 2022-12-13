#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day10")

INPUT_FILE = "inputs/day10.txt"

EXAMPLE = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

with open(INPUT_FILE) as f:
    rawdata = f.read()

if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

data = rawdata.splitlines()

cycle = [0,1]

for d in data:
    if d == "noop":
        cycle.append(cycle[-1])
    else:
        value = int(d.split(' ')[1])
        cycle.append(cycle[-1])
        cycle.append(cycle[-1] + value)

signal_strength = []
for c in [20, 60, 100, 140, 180, 220]:
    signal_strength.append(c * cycle[c])

print("Part 1:", sum(signal_strength))

drawing = ""
column = 0
for idx in range(1, len(cycle)):
    sprite_center = cycle[idx]
    if column in [sprite_center-1, sprite_center, sprite_center+1]:
        drawing += "#"
    else:
        drawing += "."
    column += 1
    if idx % 40 == 0:
        drawing += "\n"
        column = 0

print("Part 2:")
print(drawing)

