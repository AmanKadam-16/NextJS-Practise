# Now in this program we're going to takes random marks of student and sort then and retrun.
marksList = []
for i in range(6):
    i = int(i)
    mark = int(input(f'Enter mark of student for subject {i+1} : '))
    marksList.append(mark)
marksList.sort()
print('Your entered marks in sorted array are',marksList)
print(marksList)
for i in range(6):
    i = int(i)
    print(f'Your marks for sub. no. {i+1} is ', marksList[int(i)])
