def isAn(m,n):
    # s1 = []
    # s2 = []
    # t1,t2 = '',''
    # for i in m:
    #     s1.append(i)
    # for i in n:
    #     s2.append(i)
    # s1.sort()
    # s2.sort()
    # for i in s1:
    #     t1 += i
    # for i in s2:
    #     t2 += i
    return sorted(m) == sorted(n)
print(isAn('acabab','caaabb'))
print(isAn('abc','caba'))
    
    