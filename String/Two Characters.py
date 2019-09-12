#!/bin/python

import math
import os
import random
import re
import sys


def validate(s, i, j):
    l1 = len(s)
    # print l1
    s1 = ""
    count = 0
    while l1:
        if count % 2 == 0:
            s1 += i
        else:
            s1 += j
        count += 1
        l1 -= 1
    if s1 == s:
        return True
    else:
        return False


# Complete the alternate function below.
from itertools import permutations


def alternate(s):
    comb = permutations(list(set(list(s))), 2)

    char1 = list(set(list(s)))
    dict1 = {}
    max1 = 0
    for m in list(comb):
        i, j = m
        s1 = s[::]
        for c in char1:
            if c != i and c != j:
                s1 = s1.replace(c, "")
        if validate(s1, i, j):
            max1 = max(max1, len(s1))
    return max1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input().strip())

    s = raw_input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
