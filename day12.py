#!/usr/bin/python3

from copy import deepcopy
print("## AdventOfCode 2022: day12")

INPUT_FILE = "inputs/day12.txt"

EXAMPLE = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE
import sys

sys.setrecursionlimit(10000000)
hmap = rawdata.splitlines()

current_value = "a"
start_point = None
end_point = None

width = len(hmap)
length = len(hmap[0])


for row_id, row in enumerate(hmap):
    Scolumn_id = None
    Scolumn_id = None
    if "S" in row:
        Scolumn_id = row.index("S")
        start_point = (row_id, Scolumn_id)
        current_point = (row_id, Scolumn_id)
    if "E" in row:
        Ecolumn_id = row.index("E")
        end_point = (row_id, Ecolumn_id)

k = 0
goodpath = []
bad_points = []
def getNext(current_point, current_value, path):
    global end_point, length, width, goodpath, k, bad_points
    k += 1
#    if k % 100000 == 0:
 #       k=0
#    print(len(path), current_point)
    if goodpath and len(goodpath) < len(path):
        return path[:-1], False
    if current_point == end_point:
        goodpath = deepcopy(path)
        print(len(path),"vvvvvvvvvv")
        return path[:-1], False
    x, y = current_point
    
    P = []
    next_possible_steps = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
    distances = []
    next_possible_values = []

    for step in next_possible_steps:
        xx = step[0]
        yy = step[1]
        if (0 <= xx and xx <= width-1) and (0 <= yy and yy <= length-1):
            distances.append(ord(hmap[xx][yy]) - ord(current_value))
            next_possible_values.append(hmap[xx][yy])
        else:
            distances.append(100)
            next_possible_values.append(None)

    ordered_indexes = sorted(range(len(distances)),key=distances.__getitem__)  # ordonner les indexes selon la valeur
    ordered_indexes.reverse()
    for i in ordered_indexes:
        if distances[i] > 1 or next_possible_steps[i] in path or next_possible_steps[i] in bad_points:
            continue
        else:
            new_point = next_possible_steps[i]
            new_value = next_possible_values[i]
            path.append(new_point)
            path, result = getNext(new_point, new_value, path)
            if result:
                return path, True
            else:
                path = path[:-1]
                continue
    bad_points.append(current_point)
    return path[:-1], False
path, result = getNext(current_point, current_value, [current_point])
print("###########")
print(goodpath)
print(result, len(goodpath)-1)
#print("Part 1:", prod(sorted(active_monkeys)[-2:]))

#print("Part 2:", prod(sorted(active_monkeys)[-2:]))

