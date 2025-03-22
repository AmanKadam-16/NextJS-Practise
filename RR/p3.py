def isPalin(n):
    reverse = ''
    i = len(n) -1
    while i >= 0:
        print(n[i])
        reverse += n[i]
        i -= 1
    return n == reverse
print(isPalin('madam'))
print(isPalin('sir'))