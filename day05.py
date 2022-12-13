#!/usr/bin/python3

import sys
import numpy as np
import copy

print("## AdventOfCode 2022: day05")

INPUT_FILE = "inputs/day05.txt"

EXAMPLE = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

NUMBER = 0
ROW_SRC = 1
ROW_DST = 2

with open(INPUT_FILE) as f:
    rawdata = f.read()

if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

stacks_raw, orders_raw = map(str.splitlines, rawdata.split('\n\n'))

# Start from the penultimate line (which olds the range number) to the top (to have level 0 at index 0)
# end read each sub list every 4th item (to get only the numbers, separated by '] [')
stacks_transposed = [ list(x[1::4]) for x in stacks_raw[-2::-1] ]

# Transpose (columns become lines)
stacks_src = list(map(list, np.transpose(stacks_transposed)))
# Remove empty elements
stacks_src = [ [elem  for elem in s if elem != ' '] for s in stacks_src ]
# Change the orders to a list : Move X from Y to Z => [X,Y,Z]
orders = [ list(map(int, x.replace('move ', '').replace('from ', '').replace('to ', '').split(' '))) for x in orders_raw ]

stacks = copy.deepcopy(stacks_src)
for o in orders:
    crate_nb = o[NUMBER]
    src = o[ROW_SRC] - 1
    dst = o[ROW_DST] - 1
    for k in range(crate_nb):
        stacks[dst].append(stacks[src].pop())

print("Part 1:", "".join([x[-1] for x in stacks]))

stacks = copy.deepcopy(stacks_src)
for o in orders:
    crate_nb = o[NUMBER]
    src = o[ROW_SRC] - 1
    dst = o[ROW_DST] - 1
    stacks[dst] += stacks[src][-crate_nb:]
    stacks[src] = stacks[src][:-crate_nb]

print("Part 2:", "".join([x[-1] for x in stacks]))

