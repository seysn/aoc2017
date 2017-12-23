#!/usr/bin/env python3
from math import sqrt

def get_botright_edges(location):
    """
    Simply returns i as the bottom right value where the location is
    and a list of squares numbers from 1 to i with a step of 2
    """
    i = 1
    res = [1]
    while (i * i) < location:
        i += 2
        res.append(i*i)
    return i, res

assert max(get_botright_edges(13)[1]) == 25

def solve(location):
    """
    Since bottom right edges are squares numbers,
    I find the edges of the square where the location is
    and then can easily find how many steps from the start.
    """
    if location == 1: return 0
    size, edges = get_botright_edges(location)
    e = [edges[-2] + size - 1, edges[-1] - 2 * size + 2, edges[-1] - size + 1, edges[-1]]
    center = - (size // 2)

    for i in range(0, 4):
        if location <= e[i]:
            center += e[i]
            break

    return (size // 2) + abs(location - center)

assert solve(1) == 0
assert solve(12) == 3
assert solve(23) == 2
assert solve(1024) == 31

if __name__ == "__main__":
    print(solve(277678))
