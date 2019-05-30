#!/usr/bin/python3
import sys

def getOptimalValue(capacity, weights, values):
    r = 0
    data = dict(zip(weights, values))
    data = sorted(data.items(), key=lambda x: (x[0]/x[1],x[0]/x[1]), reverse=True)
    data = dict(data)
    for value, weight in data.items():
        if weight <= capacity:
            r += value
            capacity -= weight
        else:
            r += (capacity / weight) * value
            return r
    return r

if __name__ == "__main__":
    indexes     = [int(x) for x in input().split()]
    n, capacity = indexes[0:2]
    weights     = []
    values      = []
    for i in range(n):
    	element = [int(x) for x in input().split()]
    	weights.append(element[0])
    	values.append(element[1])
    optValue = getOptimalValue(capacity, weights, values)
    print("{:.4f}".format(optValue))
