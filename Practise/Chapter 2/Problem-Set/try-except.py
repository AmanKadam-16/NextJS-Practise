try:
    a = int(input('Enter any value of your choice => '))
    print('The type of your value is ',type(a))

except Exception as e:
    print('Following error occured',e)
    
finally:
    print('Thankyou for using our program 😊')