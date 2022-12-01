#!/usr/bin/python3

INPUT_FILE = "inputs/day1.txt"

if __name__ == "__main__":
    elf_calory_list = []
    with open(INPUT_FILE) as f:
        calory_list = []
        for line in f:
            if line == "\n":
                elf_calory_list.append(calory_list)
                calory_list = []
            else:
                calory_list.append(int(line[:-1]))
        if calory_list:
            elf_calory_list.append(calory_list)
        
    print(max([sum(l) for l in elf_calory_list]))
    print(sum(sorted([sum(l) for l in elf_calory_list])[-3:]))


