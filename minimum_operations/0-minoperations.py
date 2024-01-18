#!/usr/bin/python3
"""min operation"""
from math import sqrt


def minOperations(n):
    """ a function for getting min operations needed to get n number
    H when you can only copy and paste """
    if n <= 1:
        return 0
    elif is_prime(n):
        return n
    else:
        prime = small_prime(n)
        if prime:
            return prime + minOperations(int(n/prime))

