#!/usr/bin/python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a, b):
    return (a * b)  // gcd(a, b)

def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a 

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))
    