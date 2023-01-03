"""
Disparity
"""


def findDisparities(base, displaced):
    baseName, baseImage = base
    dispName, dispImage = displaced
    print(
        f'(findDisparities) Find disparities between {baseName} and {dispName}')
