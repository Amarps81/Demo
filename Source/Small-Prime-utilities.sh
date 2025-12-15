"""Small Prime utilities.

Features:
- is_prime(n): determine if integer n is prime
- nth_prime(n): returns the nth prime (2 is the 1st)
- prime_factors(n): list prime factors with multiplicity, e.g. 24 -> [2,2,2,3]
- next_prime_ge(n): first prime >= n
- gcf(a,b): greatest common factor using prime factorization
"""

from math import isqrt
from collections import Counter
from typing import List


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Return True if n is prime, False otherwise. n <= 1 -> False."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        limit = isqrt(n)
        i = 3
        while i <= limit:
            if n % i == 0:
                return False
            i += 2
        return True

    @staticmethod
    def nth_prime(n: int) -> int:
        """Return the nth prime (n >= 1). Raises ValueError for n < 1."""
        if n < 1:
            raise ValueError("n must be >= 1")
        count = 0
        num = 1
        while count < n:
            num += 1
            if Primes.is_prime(num):
                count += 1
        return num

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Return prime factorization as a list of primes (with multiplicity).
        For n == 1 returns [].
        Raises ValueError for n == 0.
        Works with negative by using abs(n).
        """
        if n == 0:
            raise ValueError("0 does not have a prime factorization")
        n = abs(n)
        if n == 1:
            return []
        factors: List[int] = []
        # factor out 2s
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # odd factors
        p = 3
        while p * p <= n:
            while n % p == 0:
                factors.append(p)
                n //= p
            p += 2
        if n > 1:
            factors.append(n)
        return factors

    @staticmethod
    def next_prime_ge(n: int) -> int:
        """Return the first prime >= n. If n <= 2 returns 2."""
        if n <= 2:
            return 2
        candidate = n
        if candidate % 2 == 0:
            # even numbers > 2 are not prime; make odd
            candidate += 1
        while not Primes.is_prime(candidate):
            candidate += 2
        return candidate

    @staticmethod
    def gcf(a: int, b: int) -> int:
        """Return greatest common factor of a and b using prime factorizations.
        Handles zeros: gcf(0, b) == abs(b), gcf(a, 0) == abs(a).
        """
        if a == 0:
            return abs(b)
        if b == 0:
            return abs(a)
        a, b = abs(a), abs(b)
        fa = Counter(Primes.prime_factors(a))
        fb = Counter(Primes.prime_factors(b))
        common = fa & fb  # intersection: min counts
        g = 1
        for p, exp in common.items():
            g *= p ** exp
        return g


if __name__ == "__main__":
    # quick demo
    print("is_prime(17):", Primes.is_prime(17))
    print("is_prime(1):", Primes.is_prime(1))
    print("6th prime (nth_prime(6)):", Primes.nth_prime(6))  # 13
    print("prime_factors(24):", Primes.prime_factors(24))  # [2,2,2,3]
    print("next_prime_ge(24):", Primes.next_prime_ge(24))  # 29
    print("gcf(48, 180):", Primes.gcf(48, 180))  # 12
