#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day09")

INPUT_FILE = "inputs/day09.txt"

EXAMPLE = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

with open(INPUT_FILE) as f:
    rawdata = f.read()

if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

data = [(x.split(' ')[0], int(x.split(' ')[1])) for x in rawdata.splitlines()]

def computeHead(H_prev, direction):
    if direction == 'R':
        H = (H_prev[0]+1, H_prev[1])
    elif direction == 'L':
        H = (H_prev[0]-1, H_prev[1])
    elif direction == 'U':
        H = (H_prev[0], H_prev[1]+1)
    elif direction == 'D':
        H = (H_prev[0], H_prev[1]-1)
    else:
        raise RuntimeError("direction is " + direction)
    return H

def computeTail(H, T_prev):
    hdistance = H[0] - T_prev[0]
    vdistance = H[1] - T_prev[1]

    T0 = T_prev[0]
    T1 = T_prev[1]
    if hdistance == 0:  # Vertical move
        T0 = T_prev[0]
        if vdistance < -1:
            T1 = T_prev[1]-1
        elif vdistance > 1:
            T1 = T_prev[1]+1
        else:
            T1 = T_prev[1]
    if vdistance == 0:  # Horizontal move
        T1 = T_prev[1]
        if hdistance < -1:
            T0 = T_prev[0]-1
        elif hdistance > 1:
            T0 = T_prev[0]+1
        else:
            T0 = T_prev[0]
    else:  # Diagonal move
        if (hdistance > 1 and vdistance >= 1) or (hdistance >= 1 and vdistance > 1):
            T0 = T_prev[0]+1
            T1 = T_prev[1]+1
        elif (hdistance < -1 and vdistance <= -1) or (hdistance <= -1 and vdistance < -1):
            T0 = T_prev[0]-1
            T1 = T_prev[1]-1
        elif (hdistance < -1 and vdistance >= 1) or (hdistance <= -1 and vdistance > 1):
            T0 = T_prev[0]-1
            T1 = T_prev[1]+1
        elif (hdistance > 1 and vdistance <= -1) or (hdistance >= 1 and vdistance < -1):
            T0 = T_prev[0]+1
            T1 = T_prev[1]-1

    return (T0,T1)

map_move = [{'H': (0,0), 'T': (0,0)}]
setT = {(0,0)}
for d in data:
    direction = d[0]
    for step in range(d[1]):
        H_prev = map_move[-1]['H']
        T_prev = map_move[-1]['T']
        H = computeHead(H_prev, direction)
        T = computeTail(H, T_prev)
        map_move.append({'H': H, 'T': T})
        setT.add(T)
print("Part 1:", len(setT))

TAIL = 9
map_move = [{'H': (0,0)}]
for k in range(1, TAIL+1):
    map_move[0][str(k)] = (0,0)

setT = {(0,0)}
for d in data:
    direction = d[0]
    for step in range(d[1]):
        H_prev = map_move[-1]['H']
        H = computeHead(H_prev, direction)
        new_pos = {'H': H}
        for k in range(1, TAIL+1):
            T_prev = map_move[-1][str(k)]
            if k == 1:
                head = new_pos["H"]
            else:
                head = new_pos[str(k-1)]
            T = computeTail(head, T_prev)
            new_pos[str(k)] = T
        map_move.append(new_pos)
        setT.add(new_pos[str(TAIL)])

print("Part 2:", len(setT))

