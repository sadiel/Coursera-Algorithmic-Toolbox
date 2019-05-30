#!/usr/bin/python3
import sys

def mergeSort(x):
    if len(x) < 2:
        return x, 0
    inv = 0
    result = []
    mid = int(len(x) / 2)
    y, invl = msort(x[:mid])
    z, invr = msort(x[mid:])
    inv = invl + invr
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
            inv += len(y) - i
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result, inv

def inversionsMergeSort(a):
    return mergeSort(a)[1]

if __name__ == '__main__':
    n = input()
    a = [int(x) for x in input().split()]
    print (inversionsMergeSort(a))
