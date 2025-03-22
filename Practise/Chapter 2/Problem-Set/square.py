try:
    i = int(input('Enter the number of which you want to find the square :'))
    print(f'The square of number {i} is {i*i}')
except Exception as e:
    print('some error occured',e)