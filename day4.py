#!/usr/bin/python3

INPUT_FILE="inputs/day4.txt"

EXAMPLE = ("2-4,6-8\n" 
"2-3,4-5\n"
"5-7,7-9\n"
"2-8,3-7\n"
"6-6,4-6\n"
"2-6,4-8")

def is1containedin2(p1, p2):
    return p2[0] <= p1[0] and p1[1] <= p2[1]

def iscontainedinother(p1, p2):
    return is1containedin2(p1,p2) or is1containedin2(p2,p1)

def is1startingin2(p1, p2):
    return p2[0] <= p1[0] and p1[0] <= p2[1]

with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE

cleaningpairs = [ x.split(',') for x in rawdata.splitlines() ]
cleaningpairs = [ [list(map(int, assignement.split('-'))) for assignement in pair] for pair in cleaningpairs ]
containedpairs = 0
for p in cleaningpairs:
    if iscontainedinother(p[0], p[1]):
        containedpairs += 1

print("part1: ", containedpairs)

overlappingpairs = 0
for p in cleaningpairs:
    # 1212 + 1221
    if is1startingin2(p[0], p[1]) or is1startingin2(p[1], p[0]):
        overlappingpairs += 1

print("part2: ", overlappingpairs)
