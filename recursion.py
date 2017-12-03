#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""IS211 Assignment 14"""


def fibonacci(n):
    """Implementing Fibonacci Sequence using recursive function."""

    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    """Implementing Euclid's GCD Algorithm using recursive function."""

    r = a % b
    if r == 0:
        return b
    else:
        (b * (a/b) + r)
        return gcd(b, r)


def compareTo(s1, s2):
    """String comparison using a recursive function."""

    if s1 == '' or s2 == '':
        return 0
    if len(s1) < len(s2):
        return compareTo(s1[1:], s2) - 1
    if len(s1) > len(s2):
        return 1 + compareTo(s1, s2[1:])
    if len(s1) == len(s2):
        return 0 + compareTo(s1[1:], s2[1:])


