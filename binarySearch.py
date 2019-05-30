#!/usr/bin/python3

def binarySearch(a, x):
    left, right = 0, (len(a) - 1)
    return binarySearchRun(a, left, right, x)

def binarySearchRun(a, left, right, x):
    if right < left:
        return -1
    mid = int(left + (right - left) / 2)
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binarySearchRun(a, mid + 1, right, x)
    else:
        return binarySsearchRun(a, left, mid-1, x)

if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    a = a[1:]
    b = [int(x) for x in input().split()]
    for x in b[1:]:
        print(binarySearch(a, x), end = ' ')
