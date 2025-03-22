# Python program to find number of zero's in a List
demoList = [4,5,9,6,0,8,0,1,3,0,8,0,7,0,6]
zeroCount = 0
for i in demoList:
    if(i == 0) :
        zeroCount += 1
print(f'The total no of zero in the List {demoList} are ',zeroCount)