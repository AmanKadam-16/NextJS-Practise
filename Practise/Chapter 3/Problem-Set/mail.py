from datetime import date

try:
    name = input('Please enter your name as per ID, ')
    currDate = date.today()
    print(f''' Congratulations {name},
          We're happy to offer you SDE role at google.. kudos..
          Joining Date: {currDate}
          🌿 ''')
except Exception as e:
    print('Error',e)
