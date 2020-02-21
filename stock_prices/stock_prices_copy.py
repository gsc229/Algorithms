#!/usr/bin/python

import argparse

""" 
   find_max_profit([10, 7, 5, 8, 11, 9]), -> 6
   find_max_profit([100, 90, 80, 50, 20, 10]), -> -10
   find_max_profit([1050, 270, 1540, 3800, 2]), -> 3530
   find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), -> 94

"""


def find_max_profit(prices):
    price_dict = {}
    current_max = prices[0]
    current_min = prices[0]

    for i in range(len(prices)):
        price_dict[prices[i]] = i
    # loop for setting max
    for j in range(price_dict[current_min], len(prices)):
        # check the index against the current max price
        # check to see if the current max index greater the current min index
        if prices[j] > current_max:
            if j > price_dict[current_max]:
                current_max = prices[j]
    # loop for setting min
    for k in range(0, len(prices)):
        if prices[k] < current_min:
            print(
                f"LESS: {k}: {prices[k]}, price_dict[current_max]{price_dict[current_max]}")
            if k < price_dict[current_max]:
                current_min = prices[k]
    if current_max == current_min:
        return prices[1] - prices[0]
    else:
        return current_max-current_min

    print([price_dict, current_min, current_max])
    print(f"prices: {prices}")
    print(f"{current_max} - {current_min} = {current_max - current_min}")

    return current_max - current_min


print(max(10, 20))
print(find_max_profit([100, 55, 4, 98, 10, 18,
                       90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))


""" if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers)) """
