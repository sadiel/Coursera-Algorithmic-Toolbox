#!/usr/bin/python3

def fibonacciSum(n):
    if n < 2:
        return n

    sum = 2
    results = [1, 1]
    for _ in range(n%60):
        current = (results[-1] % 10 + results[-2] % 10) % 10
        results.append(current % 10)
        sum += current

    return (results[-1] - 1) % 10

import sys

if __name__ == '__main__':
    n = int(input())
    print(fibonacciSum(n))
