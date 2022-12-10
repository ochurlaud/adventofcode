#!/usr/bin/python3

print("## AdventOfCode 2022: day07")

INPUT_FILE = "inputs/day07.txt"

EXAMPLE = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open(INPUT_FILE) as f:
    rawdata = f.read()

##rawdata = EXAMPLE

def path2dtree(d, path):
    if path in ["", "/"]:
        return d
    current_pos = d
    for p in path.split('/'):
        current_pos = current_pos["dirs"][p]
    return current_pos

tree = {'dirs': {}, 'files': []}
current_path = ""
for l in rawdata.splitlines():
    splitted_line = l.split(' ')
    # if it's a command
    if splitted_line[0] == '$':
        if splitted_line[1] == "cd":
            current_dir = splitted_line[2]
            if current_dir == "..":
                current_path = "/".join(current_path.split("/")[:-1])
            elif current_dir == "/":
                current_path = ""
            else:
                if current_path == "":
                    current_path = current_dir
                else:
                    current_path += "/" + current_dir
        elif splitted_line[1] == "ls":
            pass
    # otherwise it's a command result
    else:
        dir_or_size = splitted_line[0]
        name = splitted_line[1]
        dtree = path2dtree(tree, current_path)
        if dir_or_size == "dir":
            dtree["dirs"][name] = {'dirs': {}, 'files': [] }
        else:
            dtree["files"].append({'name': name, 'size': int(dir_or_size)})

def compute_dirsizes(subtree):
    
    tree_size = 0
    tree_size += sum( [x["size"] for x in subtree["files"]] )
    for d in subtree["dirs"]:
        dirsize = compute_dirsizes(subtree["dirs"][d])
        tree_size += dirsize
    subtree["size"] = tree_size
    return tree_size

compute_dirsizes(tree)

MAX_SIZE = 100000

def sum_dirsizes(subtree, maxsize):
    sumsize = 0
    for d in subtree["dirs"]:
        if subtree["dirs"][d]["size"] <= MAX_SIZE:
            sumsize += subtree["dirs"][d]["size"]
        sumsize += sum_dirsizes(subtree["dirs"][d], maxsize)
    return sumsize


print("Part 1:", sum_dirsizes(tree, MAX_SIZE))

NEEDED_FREE_SPACE = 30000000
DISK_SIZE = 70000000
used_size = tree['size']

MIN_SIZE = NEEDED_FREE_SPACE + used_size - DISK_SIZE

def list_dirsizes(subtree, minsize):
    sumsize = []
    for d in subtree["dirs"]:
        if subtree["dirs"][d]["size"] >= minsize:
            sumsize.append(subtree["dirs"][d]["size"])
        sumsize += list_dirsizes(subtree["dirs"][d], minsize)
    return sumsize

print("Part 2:", min(list_dirsizes(tree, MIN_SIZE)))

