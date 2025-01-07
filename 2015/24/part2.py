#!/usr/bin/env python
""" Day 24 """

import operator
import sys

with open(sys.argv[1]) as infile:
    WEIGHTS = set([int(x.strip()) for x in infile])

K = sum(WEIGHTS)

# ideal subset is floor(K / 3), where K = sum(WEIGHTS)
def find_partition():
    """ Partition set into 3 equal parts """
    n = len(WEIGHTS)
    k = sum(WEIGHTS)
    p = [] * ((k/3) + 1)
    p.append([True] * (n+1))
    for _ in xrange(k/3 + 1):
        p.append([False])
        p[-1].extend([None] * n)

    #print p
    for i in xrange(1, k/3+1):
        for j in xrange(1, n+1):
            p[i][j] = p[i][j-1] or p[i][j-1]

find_partition()

# so, let's look for a subset that sums to that value
TARGET = K / 4
SOLUTIONS = []

def find_subset(items, target, current=set(), keepers=None):
    """ subset sum """

    if len(current) > 4:  # this looks like about as small as it gets
        return

    if sum(items) == target:
        inspect = current | items
        if inspect in SOLUTIONS:
            return set()

        return set()

    for item in sorted(items, reverse=True):
        inspect = current | set([item])

        if inspect in SOLUTIONS:
            continue

        SOLUTIONS.append(inspect)

        if target - item == 0:
            if sum(WEIGHTS - inspect) == 3 * TARGET:
                product = reduce(operator.mul, inspect)
                print len(inspect), product, inspect
                keepers.append(inspect)

            return inspect

        if target - item < 0:
            return set()

        if sum(items - set([item])) < target:
            return set()

        find_subset(items - set([item]), target - item, current=inspect, keepers=keepers)

KEEPERS = []
find_subset(WEIGHTS, TARGET, keepers=KEEPERS)

print '\n'.join([str(x) for x in KEEPERS])

