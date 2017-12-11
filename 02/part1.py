#!/usr/bin/env python3

def diff(row):
    values = [int(i) for i in row.split()]
    if len(values) == 0: return 0
    return max(values) - min(values)

def solve(content):
    return sum([diff(line) for line in content.split("\n")])

assert diff("5 1 9 5") == 8
assert diff("7 5 3") == 4
assert diff("2 4 6 8") == 6
assert solve("5 1 9 5\n7 5 3\n2 4 6 8") == 18

if __name__ == "__main__":
    with open("input.txt") as f:
        print(solve(f.read()))
