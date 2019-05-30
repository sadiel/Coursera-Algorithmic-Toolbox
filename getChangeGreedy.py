#!/usr/bin/python3
import sys

def getChange(m):
	r = 0
	coins = [10, 5, 1]
	for c in coins:
		while m - c >= 0:
			m -= c
			r += 1
	return r

if __name__ == '__main__':
    m = int(input())
    print(getChange(m))
