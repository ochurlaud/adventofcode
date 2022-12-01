#!/usr/bin/python3

INPUT_FILE = "inputs/day1.txt"

if __name__ == "__main__":
    with open(INPUT_FILE) as f:
        elf_calory_list = [ [int(i) for i in s.split('\n')] for s in f.read()[:-1].split('\n\n') ]  # [:-1] to remove the last '\n'
        
    print(max([sum(l) for l in elf_calory_list]))
    print(sum(sorted([sum(l) for l in elf_calory_list])[-3:]))


