# a prime number is the number thats
# divisible only by itself and one only
import math
def isPrime(n):
    n = int(n)
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True
print(isPrime(811))