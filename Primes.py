

# Based on this video:
# https://www.youtube.com/watch?v=_gCKX6VMvmU


import math
from decimal import *

# Set decimal precision of numbers
getcontext().prec = 10000

# Use file containing list of primes to generate the constant
def genConst():
    c = Decimal(1)
    total = Decimal(1)
    primes = getPrimesList()
    for i in range(1,len(primes)):
        total = total * primes[i-1]
        c += (primes[i] - 1) / total

    with open("primeConstant.txt","w") as f:
        f.write(str(c))


# Use constant to generate list of N primes
def primeList(n):
    c = getConst()
    l = [c]
    for i in range(n-1):
        l += [math.floor(l[i]) * (l[i] - math.floor(l[i]) + 1)]
    for i in range(n):
        l[i] = math.floor(l[i])
    return l


# Use constant to generate the Nth prime
def prime(n):
    p = getConst()
    for _ in range(n-1):
        p = math.floor(p) * (p - math.floor(p) + 1)
    return math.floor(p)


def getConst():
    with open("primeConstant.txt","r") as f:
        c = Decimal(f.read())
    return c

def getPrimesList():
    with open("primes.txt","r") as f:
        txt = f.readlines()[0].split(",")
    p = []
    for n in txt:
        p += [Decimal(n)]
    return p


def testAccuracy():
    p = 2
    primes = getPrimesList()
    i = 1
    while p == primes[i-1]:
        i += 1
        p = prime(i)
    print("Accurate for first " + str(i-1) + " primes")
    




