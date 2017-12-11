#!/usr/bin/env python3

def diff(row):
    values = sorted([int(i) for i in row.split() if int(i)], reverse=True)
    for i in range(len(values)):
        for j in values[i+1:]:
            tmp = values[i] / j
            if int(tmp) == tmp:
                return int(tmp)
    return 0

def solve(content):
    return sum([diff(line) for line in content.split("\n")])

assert diff("5 9 2 8") == 4
assert diff("9 4 7 3") == 3
assert diff("3 8 6 5") == 2
assert solve("5 9 2 8\n9 4 7 3\n3 8 6 5") == 9

if __name__ == "__main__":
    with open("input.txt") as f:
        print(solve(f.read()))
