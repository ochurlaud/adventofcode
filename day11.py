#!/usr/bin/python3

import sys

print("## AdventOfCode 2022: day11")

INPUT_FILE = "inputs/day11.txt"

EXAMPLE = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

with open(INPUT_FILE) as f:
    rawdata = f.read()


def solve_plus(old, v):
    #old = a*d+r
    for d in old:
        a = old[d][0]
        r = old[d][1]
        r = r + v
        a += r // d
        r = r % d
        old[d] = (a,r)
    return old

def solve_times(old, v):
    global optimize
    #old = a*d+r
    for d in old:
        r = old[d][1]
        a = old[d][0]
        if optimize:
            a = 0
        else:
            a = a*v
        r = r*v
        a += r // d
        r = r % d
        old[d] = (a,r)
    return old

def solve_square(old):
    global optimize
    for d in old:
        a = old[d][0]
        r = old[d][1]
        if optimize:
            a = 0
        else:
            a = a*a*d + 2*a*r
        r = r*r
        a += r // d
        r = r % d
        old[d] = (a,r)
    return old

def monkeyops(sign, value):
    if sign == '+':
        return lambda old: solve_plus(old, int(value))
    elif sign == "*":
        if value == "old":
            return lambda old: solve_square(old)
        else:
            return lambda old: solve_times(old, int(value))
    else:
        raise RuntimeError("NEVER HAPPENS")


if len(sys.argv) > 1 and sys.argv[1] == "ex":
    rawdata = EXAMPLE

monkey_data = rawdata.split('\n\n')

def init_monkeys(monkey_data):
    monkeys = []
    for i, one_monkey_raw in enumerate(monkey_data):
        one_monkey = one_monkey_raw.splitlines()
        items = list(map(int, one_monkey[1].split(': ')[-1].split(', ')))

        opswords = one_monkey[2].split()

        operation = monkeyops(opswords[-2], opswords[-1])
        test_divisible_by = int(one_monkey[3].split(' ')[-1])
        result = {
                    True: int(one_monkey[4].split(' ')[-1]),
                    False: int(one_monkey[5].split(' ')[-1])
                }
        monkeys.append(
                {
                    'items': items,
                    'operation': operation,
                    'test': test_divisible_by,
                    'result': result
                }
            )
    divisors = [ m['test'] for m in monkeys ]

    for m in monkeys:
        items = []
        for item in m['items']:
            items.append(compute_item(item, divisors))
        m['items'] = items

    return monkeys, divisors

def compute_item(item, divisors):
    if type(item) == type(3):
        item_reduced = {}
        for d in divisors:
            item_reduced[d] = (item // d, item % d)
        return item_reduced

def is_divisible_by(item, d):
    return item[d][1] == 0

def item_value(item):
    d = list(item.keys())[0]
    return d*item[d][0] + item[d][1]

monkeys,divisors = init_monkeys(monkey_data)
optimize = False
def play_round(monkeys, active_monkeys, worry_division, divisors):
    for monkey_id in range(len(monkeys)):
        #print("## MONKEY", monkey_id)
        monkey =  monkeys[monkey_id]
        for item in monkey['items']:
            #print("init:",item_value(item))
            item = monkey['operation'](item)
            #print("after:", item_value(item))
            if worry_division != 1:
                v = item_value(item)
                new_v = int(float(v)/worry_division)
                item = compute_item(new_v, divisors)
                #print("divided:", item_value(item))
            test = is_divisible_by(item, monkey['test'])
            next_monkey = monkey['result'][test]
            #debug("next:", next_monkey)
            monkeys[next_monkey]['items'].append(item)
            active_monkeys[monkey_id] += 1
        monkeys[monkey_id]['items'] = []

active_monkeys = [0 for m in monkeys]
for r in range(20):
    #print("===== ROUND", r, "=====")
    play_round(monkeys, active_monkeys, 3, divisors)
from math import prod
print("Part 1:", prod(sorted(active_monkeys)[-2:]))


optimize = True
monkeys,divisors = init_monkeys(monkey_data)
active_monkeys = [0 for m in monkeys]
for r in range(10000):
#    print("\rRound", r, end="")
    play_round(monkeys, active_monkeys, 1, divisors)
#print()
print("Part 2:", prod(sorted(active_monkeys)[-2:]))

