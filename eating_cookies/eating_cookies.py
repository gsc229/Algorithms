#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


# Permutaion: n P r   ==> n!/(n-r)!

# x - n  =


# case 3 - 4 dif: 1
# 1 1 1
# 1 2
# 2 1
# 3

# case 4 - 6 dif: 2
# 2 1 1
# 1 2 1
# 1 1 2
# 3 1
# 1 3

# case 5 - 8 dif: 3
# 1 1 1 1 1
# 2 1 1 1
# 1 2 1 1
# 1 1 2 1
# 1 1 1 2
# 3 1 1
# 1 3 1
# 1 1 3

# case 6 - 10 dif: 4
# 1 1 1 1 1 1
# 2 1 1 1 1
# 1 2 1 1 1
# 1 1 2 1 1
# 1 1 1 2 1
# 1 1 1 1 2
# 3 1 1 1
# 1 3 1 1
# 1 1 3 1
# 1 1 1 3
count = 0


def eating_cookies(n, cache=None):
    global count
    if n == 0:
        count += 1
        return 1
    if n < 0:
        return 0

    # eat three see what happens n - 3
    eating_cookies(n-3)

    # eat two see what happnes n - 2
    eating_cookies(n-2)

    # eat one see what happens n - 1
    eating_cookies(n-1)

    return count


print(eating_cookies(1))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
