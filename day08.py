#!/usr/bin/python3

print("## AdventOfCode 2022: day08")

INPUT_FILE = "inputs/day08.txt"

EXAMPLE = """30373
25512
65332
33549
35390"""

with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE

data = rawdata.splitlines()
width = len(data[0])
length = len(data)

visible_trees = []
# we don't care about the edges
for i in range(1, length-1):
    for j in range(1, width-1):
        tree_high = data[i][j]
        is_visible = []
        for i2 in range(i):
            if data[i][j] <= data[i2][j]:
                is_visible.append(False)
                break
        for i2 in range(i+1, length):
            if data[i][j] <= data[i2][j]:
                is_visible.append(False)
                break
        for j2 in range(j):
            if data[i][j] <= data[i][j2]:
                is_visible.append(False)
                break
        for j2 in range(j+1, width):
            if data[i][j] <= data[i][j2]:
                is_visible.append(False)
                break
        if len(is_visible) < 4: # dans ce cas visible
            visible_trees.append((i,j))

print("Part 1:", len(visible_trees) + 2 * (width + length - 2))
treeview = []
for i in range(1, length-1):
    for j in range(1, width-1):
        tree_high = data[i][j]
        a,b,c,d = 0,0,0,0
        for i2 in range(i-1, -1, -1):
            a += 1
            if data[i2][j] >= data[i][j]:
                break;
        for i2 in range(i+1, length):
            b += 1
            if data[i2][j] >= data[i][j]:
                break;
        for j2 in range(j-1, -1, -1):
            c += 1
            if data[i][j2] >= data[i][j]:
                break;
        for j2 in range(j+1, width):
            d += 1
            if data[i][j2] >= data[i][j]:
                break;
        treeview.append(a*b*c*d)

print("Part 2:", max(treeview))

