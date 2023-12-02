"""Importing random module for randint"""
import random
import numpy as np

DEFAULT_ACCURACY = 3


def sumtwovalues(first, second):
    """Summary of two values."""
    return first + second


def div(x, y, accuracy):
    """Divide x by y with accuracy."""
    return round(x/y,  accuracy)


def get_rand():
    """Gets random."""
    return random.randint(1, 10)


def rand_array():
    """Gets random array."""
    a = [get_rand(), get_rand(), get_rand()]
    return np.array(a)


def main():
    """Main function."""


main()
