#!/usr/bin/env python3

def solve(captcha):
    cpt = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[i - 1]:
            cpt += int(captcha[i])
    return cpt

assert solve("1122") == 3
assert solve("1111") == 4
assert solve("1234") == 0
assert solve("91212129") == 9

if __name__ == "__main__":
    with open("input.txt") as f:
        print(solve(f.readline()[:-1]))
