try:
    x = int(input('Enter a number'))
    y = int(input('Enter another number'))
    print(f'The average of two nunmbers {x} and {y} is {(x+y)/2}')
except Exception as e:
    print('Some error occured... try again.. Reason: ',e)