#! /usr/bin/env python3
"""Problem: Largest prime factor of 600851475143
Solution: 6857
Author: AnonymouX47
"""

# Note: (not n % p) is basically the same as (n % p == 0) but better :)

def largest_prime_factor(num):
    """Returns the largest prime factor of 'num'"""

    while not num % 2:
        num //= 2
    if num == 1:
        return 2
    n = 1
    while num > 1:
        # With 2 aside, Only odd numbers can be prime
        n += 2  # next odd number

        # It's just like the normal process to get prime factors in maths.
        # Keep dividing num by n until num is no longer evenly divisible by n.
        while not num % n:
            num //= n

    return n  # The number to finish dividing num is the largest

num = 600851475143

n = largest_prime_factor(num)
print("%d is the largest prime factor of %d" % (n, num))
