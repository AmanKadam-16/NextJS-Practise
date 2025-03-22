# factorial is nothing but multiplication of given number in rever order till 1

def fact(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
print(fact(4))

def recur_fact(n):
    if n == 0 or n == 1:
        return 1
    return n*recur_fact(n-1)
print(recur_fact(5))