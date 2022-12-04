#!/usr/bin/python3

print("## AdventOfCode 2022: day1")

INPUT_FILE = "inputs/day1.txt"

EXAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def max_calories_carried(calories_list):
    return max(map(sum, calories_list))

def sorted_calories_carried(calories_list):
    return sorted(map(sum, calories_list))

with open(INPUT_FILE) as f:
    rawdata = f.read()

#rawdata = EXAMPLE

# cut on double newlines and make sublist of ints of each line.
elf_calories_list = [ list(map(int, s.splitlines())) for s in rawdata.split('\n\n') ]


print("Part 1: ", max_calories_carried(elf_calories_list))

print("Part 2: ", sum(sorted_calories_carried(elf_calories_list)[-3:]))


