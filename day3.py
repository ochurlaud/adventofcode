#!/usr/bin/python3

print("## AdventOfCode 2022: day3")

INPUT_FILE = "inputs/day3.txt"

EXAMPLE = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def priority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27  # A = 27, B = 28,...
    else:
        return ord(c) - ord('a') + 1  # a = 1, b = 2,...

with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE

backpacks = rawdata.splitlines()
duplicate_items = []
for b in backpacks:
    bsize = len(b)
    compartiment1 = b[:bsize//2]
    compartiment2 = b[bsize//2:]
    current_duplicate_items = []
    for item in compartiment1:
        if item in compartiment2 and item not in current_duplicate_items:
            current_duplicate_items.append(item)
    duplicate_items += current_duplicate_items
ps = [priority(x) for x in duplicate_items]
print("Part 1: ", sum(ps))

duplicate_items = []
for k in range(len(backpacks)//3):
    current_duplicate_items = []
    for item in backpacks[3*k]:
        if item in backpacks[3*k+1] and item in backpacks[3*k+2] and item not in current_duplicate_items:
            current_duplicate_items.append(item)
    duplicate_items += current_duplicate_items

ps = [priority(x) for x in duplicate_items]
print("Part2 : ", sum(ps))
