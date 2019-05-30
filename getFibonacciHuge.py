#!/usr/bin/python3

import math

def pisano(m):
    previous = 1
    current = 1
    result = 1
    while not (previous == 0 and current == 1):
        buffer = (previous + current) % m
        previous = current
        current = buffer
        result += 1

    return result

def fibonacci(n, m):
    if n < 2:
        return n

    results = [1, 1]
    for _ in range(n - 2):
        results.append((results[-1] + results[-2]) % m)

    return results[-1]

def getFibonacciHuge(n, m):
    return fibonacci(n % pisano(m), m)

import sys

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(getFibonacciHuge(n, m))
