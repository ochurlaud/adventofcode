#!/usr/bin/python3

print("## AdventOfCode 2022: day06")

INPUT_FILE = "inputs/day06.txt"

EXAMPLE = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
EXAMPLE = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""
with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE


def start_marker_position(data, size):
    start_block = []
    for i, char in enumerate(data):
        if char in start_block: 
            index = start_block.index(char)
            start_block = start_block[index+1:] + [char]
        else:
            start_block.append(char)
            if len(start_block) == size:
                return i + 1

START_BLOCK_SIZE = 4
print("Part 1:", start_marker_position(rawdata, START_BLOCK_SIZE))
START_BLOCK_SIZE = 14
print("Part 2:", start_marker_position(rawdata, START_BLOCK_SIZE))

