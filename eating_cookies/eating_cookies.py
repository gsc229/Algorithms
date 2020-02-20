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


def eating_cookies(n, cache=None):

    if n == 0:
        return 1
    if n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache
    else:
        if cache == None:
            cache = {}
        # suppose n = 3, then:
        #       e.c(0)->(returns 1) + e.c(1)->(returns 1) + e.c(2)->(returns 2)   --> value = 4
        value = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
        # cache{3: 4}
        cache[n] = value
        return value


print(eating_cookies(5, {}))

"""
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if cache is None:
            cache = {}
        value = eating_cookies(
            n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        cache[n] = value
        return value

"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
