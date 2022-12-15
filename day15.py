#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day15")

INPUT_FILE = "inputs/day15.txt"

EXAMPLE = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

with open(INPUT_FILE) as f:
    rawdata = f.read()
    
LINE = 2000000
MAX_XY = 4000000
MIN_XY = 0
if len(sys.argv) > 1 and sys.argv[1] == "ex":
    LINE = 10
    MAX_XY = 20
    rawdata = EXAMPLE

data = [l.split() for l in rawdata.splitlines()]

sX = []
sY = []
bX = []
bY = []

for d in data:
    sX.append(int(d[2].replace('x=', '').replace(',', '')))
    sY.append(int(d[3].replace('y=', '').replace(':', '')))
    bX.append(int(d[8].replace('x=', '').replace(',', '')))
    bY.append(int(d[9].replace('y=', '')))

def searchinline(line, sX, sY, bX, bY, minmax=None):
    notin = set({})
    for i in range(len(sX)):
        #print("source=",sX[i], sY[i])
        #print("beacon=", bX[i], bY[i])
        d_sb = abs(sX[i] - bX[i]) + abs(sY[i] - bY[i])
        #print(d_sb)
        if sY[i] - d_sb <= line and line <= sY[i] + d_sb:
            l = abs(sY[i] - line)
            range_min = sX[i]-(d_sb-l)
            range_max = sX[i]+(d_sb-l)
            if minmax:
                range_min = max(range_min, minmax[0])
                range_max = min(range_max, minmax[1])
            for x in range(range_min, range_max+1):
                if not minmax or minmax[0] <= x and x <= minmax[1]:
                    y = line
                    if (x,y) not in [(sX[i],sY[i]), (bX[i], bY[i])] and y == line:
                        notin.add((x,y))
                    else:
                        #print("beacon or source")
                        pass
                else:
                    print(x)
                    pass
    return notin

notin = searchinline(LINE, sX, sY, bX, bY)
print("Part 1:", len(notin))

beacon = None
for y in range(MIN_XY, MAX_XY+1):
    print(y)
    if beacon:
        break
    notin = set({})
    if y in sY:
        i = sY.index(y)
        notin.update({(sX[i],sY[i])})
    if y in bY:
        i = bY.index(y)
        notin.update({(bX[i], bY[i])})
    notin.update(searchinline(y, sX, sY, bX, bY, [MIN_XY, MAX_XY]))
    for i in range(MIN_XY, MAX_XY+1):
        if (i,y) not in notin:
            beacon = (i,y)
            break

print("Part 2:", beacon[0]*4000000 + beacon[1])
