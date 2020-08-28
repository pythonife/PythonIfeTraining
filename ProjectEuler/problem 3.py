#! /usr/bin/env python3
"""Problem: Largest prime factor of 600851475143
Solution: 6857
Author: AnonymouX47
"""

# Note: (not n % p) is basically the same as (n % p == 0) but better :)

def is_prime(n):
    """Checks if n is prime
    This approach is generally only applicable when the
    program entails testing of consecutively ascending numbers.
    """

    # Every composite (non-prime) number is evenly divisble
    # by at least one prime less than itself

    # A function can *access* a name dedined outside itself i.e 'primes'

    for p in primes:
        if not n % p:
            # n is not prime
            return False
    else:
        # n is prime
        primes.append(n)
        return True


def largest_prime_factor(num):
    """Returns the largest prime factor of 'num'"""

    if not num % 2:
        # the only and largest prime factor of any even number is 2
        return 2
    n = 1
    while num > 1:
        # With 2 aside, Only odd numbers can be prime

        n += 2  # next odd number

        # it takes less time to check for divisibility than to check for primality
        # so check for divisibility first

        if not num % n and is_prime(n):
            # Keep dividing num by n until num is no longer evenly divisible by n.
            while not num % n:
                num //= n
    return n

primes = []
num = 600851475143

n = largest_prime_factor(num)
print("%d is the largest prime factor of %d" % (n, num))
