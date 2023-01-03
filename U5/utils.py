"""
Image Utils
"""

from numpy import arange, interp, ceil


def mapValueToRange(value, fromRange, toRange, step):
    fp = arange(toRange[0], toRange[1], step)
    xp = arange(fromRange[0], fromRange[1], fromRange[1]/len(fp))
    return interp(value, xp, fp)


def findNearestOddInt(number):
    return int(ceil(number) // 2 * 2 + 1)
