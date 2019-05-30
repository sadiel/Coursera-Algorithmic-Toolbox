#!/usr/bin/python3

def getChange(money, coins):
    MinNumCoins = (money+1) * [0]
    MinNumCoins[0] = 0
    for m in range(1, money + 1):
    	MinNumCoins[m] = 1000000
    	for coin in coins:
    		if m >= coin:
    			NumCoins = MinNumCoins[m - coin] + 1
    			if NumCoins < MinNumCoins[m]:
    				MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(input())
    print(getChange(m, [1, 3, 4]))
