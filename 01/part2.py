#!/usr/bin/env python3

def solve(captcha):
    cpt = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + len(captcha) // 2) % len(captcha)]:
            cpt += int(captcha[i])
    return cpt

assert solve("1212") == 6
assert solve("1221") == 0
assert solve("123425") == 4
assert solve("123123") == 12
assert solve("12131415") == 4

if __name__ == "__main__":
    with open("input.txt") as f:
        print(solve(f.readline()[:-1]))
