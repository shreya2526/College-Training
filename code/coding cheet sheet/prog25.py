#Best time to buy and sell stock

import sys

def stock_sell_price(price):
    min_val = sys.maxsize
    max_val = -sys.maxsize - 1

    for i in range(len(price)):
        min_val=min(min_val,price[i])
        max_val=max(max_val, price[i]-min_val)
    return max_val

price=[7,1,3,4,5,6]
print(stock_sell_price(price))