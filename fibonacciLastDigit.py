#!/usr/bin/python3

def fibonacciLastDigit(n):
    if n == 0:
        return 0
    f = list(range(0, n + 1))
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
    	f[i] = f[i-1] % 10 + f[i-2] % 10

    return f[n] % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacciLastDigit(n))
