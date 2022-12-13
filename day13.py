#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day13")

INPUT_FILE = "inputs/day13.txt"

EXAMPLE = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

with open(INPUT_FILE) as f:
    rawdata = f.read()
    
if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

pairs = [ list(map(eval, r.splitlines())) for r in rawdata.split('\n\n') ]

def compare(p1, p2):
    INF = -1
    EQUAL = 0
    SUP = 1
    if type(p1) == type(3) and type(p2) == type(3):
        if p1 == p2:
            return EQUAL
        elif p1 < p2:
            return INF
        elif p1 > p2:
            return SUP
    
    if type(p1) != type([]):
        p1 = [p1]
    elif type (p2) != type([]):
        p2 = [p2]
    else:
        pass # Both are list we are fine

    for k in range(len(p1)):
        if k == len(p2):
            return SUP
        else:
            rvalue = compare(p1[k], p2[k])
            if rvalue == EQUAL:
                continue
            elif rvalue == SUP:
                return SUP
            else:
                return INF
    # If we arrive here it means that p1 equal to the beginning of p2
    if len(p1) == len(p2):
        return EQUAL
    elif len(p1) < len(p2):
        return INF

    print("IMPOSSIBLE", p1, p2)
    return EQUAL


rightorder = []
for i,p in enumerate(pairs):
    p1 = p[0]
    p2 = p[1]
    if compare(p1,p2) in [0,-1]:
        rightorder.append(i+1)

print("Part 1:", sum(rightorder))

class L():
    def __lt__(self, other):
        return compare(self.l, other.l) == -1
    def __le__(self, other):
        return compare(self.l, other.l) in [0,-1]
    def __ge__(self, other):
        return compare(self.l, other.l) in [0,1]
    def __gt__(self, other):
        return compare(self.l, other.l) in [1]
    def __eq__(self, other):
        return compare(self.l, other.l) in [0]

    def __init__(self, l):
        self.l = l
    def __repr__(self):
        return self.l.__repr__()

everything = list(map(lambda l:L(eval(l)), rawdata.replace('\n\n','\n').splitlines()))

everything.append(L([[2]]))
everything.append(L([[6]]))
sortedlist = [ x.l for x in sorted(everything)]
result = (sortedlist.index([[2]])+1) * (sortedlist.index([[6]])+1)
print("Part 2:", result)

