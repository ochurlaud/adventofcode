#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day14")

INPUT_FILE = "inputs/day14.txt"

EXAMPLE = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

with open(INPUT_FILE) as f:
    rawdata = f.read()
    
if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

data = [ list(map(lambda y: (int(y.split(',')[0]),int(y.split(',')[1])), x.split(' -> '))) for x in rawdata.splitlines()]

SAND_SRC = (500,0)

# init map
def init_map(data, SAND_SRC):
    xvalues = [ x[0] for y in data for x in y]
    yvalues = [ x[1] for y in data for x in y]
    grid=[[(x,y) for x in range(min(xvalues), max(SAND_SRC[0],max(xvalues)+1)) ] for y in range(min(SAND_SRC[1], min(yvalues)), max(yvalues)+1) ]
    rocks=[['.' for c in r] for r in grid]

    sand_src_id = None
    for rid in range(len(grid)):
        for cid in range(len(grid[0])):
            if grid[rid][cid] == SAND_SRC:
                rocks[rid][cid] = "+"
                sand_src_id = (rid,cid)
                break
        if sand_src_id:
            break

    for rid, row in enumerate(grid):
        for cid, cell in enumerate(row):
            for d in data:
                for i in range(len(d)):
                    if i+1 == len(d):
                        continue
                    else:
                        if d[i][0] <= cell[0] and cell[0] <= d[i+1][0] and cell[1] == d[i][1] and cell[1] == d[i+1][1] or \
                           d[i+1][0] <= cell[0] and cell[0] <= d[i][0] and cell[1] == d[i][1] and cell[1] == d[i+1][1] or \
                           d[i][1] <= cell[1] and cell[1] <= d[i+1][1] and cell[0] == d[i][0] and cell[0] == d[i+1][0] or \
                           d[i+1][1] <= cell[1] and cell[1] <= d[i][1] and cell[0] == d[i][0] and cell[0] == d[i+1][0]:
                               rocks[rid][cid] = "#"
    return sand_src_id, rocks
    #print('\n'.join([''.join(x) for x in rocks]))

def next_step(current_space, rocks):
    global sand_src_id
    r,c = current_space
    if rocks[r+1][c] == '.':
        return next_step((r+1,c), rocks)
    elif c == 0:
        return None, rocks
    elif rocks[r+1][c-1] == '.':
        return next_step((r+1,c-1), rocks)
    elif c == len(rocks[0])-1 :
        return None, rocks
    elif rocks[r+1][c+1] == ".":
        return next_step((r+1,c+1), rocks)
    else:
        rocks[r][c] = 'o'
        return current_space, rocks

sand_src_id, rocks = init_map(data, SAND_SRC)
stop = 1
step_nb = 0
while stop not in [sand_src_id, None]:
    step_nb += 1
    stop, rocks = next_step(sand_src_id, rocks)
    if stop == None:
        step_nb -=1  # If stop is None it means that we didn't add an element on top of the pile
print('\n'.join([''.join(x) for x in rocks]))
    
print("Part 1:", step_nb)

xvalues = [ x[0] for y in data for x in y]
yvalues = [ x[1] for y in data for x in y]
maxy = max(yvalues)
data2 = data+ [[ (min(xvalues)-1000, maxy+2), (max(xvalues)+1000,maxy+2)]]

sand_src_id, rocks = init_map(data2, SAND_SRC)
stop = 1
step_nb = 0
while stop not in [sand_src_id, None]:
    step_nb += 1
    stop, rocks = next_step(sand_src_id, rocks)
    if stop == None:
        step_nb -=1  # If stop is None it means that we didn't add an element on top of the pile
print('\n'.join([''.join(x) for x in rocks]))

print("Part 2:", step_nb)

