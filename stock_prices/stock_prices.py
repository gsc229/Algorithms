#!/usr/bin/python

import argparse

""" 
   find_max_profit([10, 7, 5, 8, 11, 9]), -> 6
   find_max_profit([100, 90, 80, 50, 20, 10]), -> -10
   find_max_profit([1050, 270, 1540, 3800, 2]), -> 3530
   find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), -> 94

"""


def find_max_profit(prices):
    max_profit = 0
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            max_profit = max(max_profit, prices[j]-prices[i])

    if max_profit == 0:
        max_profit = prices[len(prices)-1] - prices[len(prices)-2]

    return max_profit


print(find_max_profit([100, 90, 80, 50, 20, 10]))


""" if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers)) """
