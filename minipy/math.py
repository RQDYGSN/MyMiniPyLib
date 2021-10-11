"""
Some basic mathematical tools
"""


def getGreatestCommonDivisor(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def getLeastCommonMultiple(a, b):
    return a*b/getGreatestCommonDivisor(a, b)
