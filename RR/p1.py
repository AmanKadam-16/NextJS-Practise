import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
print(isPrime(3))
print(isPrime(4))
