try:
    a = int(input('Enter value one : '))
    b = int(input('Enter value two : '))
    if(a>b):
        print(f'{a} is greater than {b}')
    elif(a==b):
        print(f'Both {a} and {b} are equal values.')
    else:
        print(f'{b} is greater than {a}')
except Exception as e:
    print('Some error occured : ',e)
finally:
    print('Btw.. nice playing with you.. see u soon')

