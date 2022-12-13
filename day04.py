#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day04")

INPUT_FILE = "inputs/day04.txt"

EXAMPLE = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def is1containedin2(p1, p2):
    return p2[0] <= p1[0] and p1[1] <= p2[1]

def iscontainedinother(p1, p2):
    return is1containedin2(p1,p2) or is1containedin2(p2,p1)

def is1startingin2(p1, p2):
    return p2[0] <= p1[0] and p1[0] <= p2[1]

with open(INPUT_FILE) as f:
    rawdata = f.read()

if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

cleaningpairs = [ x.split(',') for x in rawdata.splitlines() ]
cleaningpairs = [ [list(map(int, assignement.split('-'))) for assignement in pair] for pair in cleaningpairs ]
containedpairs = 0
for p in cleaningpairs:
    if iscontainedinother(p[0], p[1]):
        containedpairs += 1

print("Part 1:", containedpairs)

overlappingpairs = 0
for p in cleaningpairs:
    if is1startingin2(p[0], p[1]) or is1startingin2(p[1], p[0]):
        overlappingpairs += 1

print("Part 2:", overlappingpairs)
