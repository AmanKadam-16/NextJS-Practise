# a palindrome string / number when read from l to r or r to l reads same.

def isPalin(s):
    rev = ''
    i = len(s) - 1
    while i >=0:
        rev += s[i]
        i -= 1
    return rev == s
print(isPalin('madam'))
print(isPalin('sir'))

def isPalin2(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(isPalin2('eye'))
print(isPalin2('watch'))