# The next learning is about string
a = 'John'
b = "John Doe"
c = ''' John
Doe is an example name. '''
# So above were three ways of representing string. 
# I guess why they not support backticks to for string as in JS like let a  =  `Hey!`

# Also in Python we can slice string and access them as per their index.
# And to my surprise the indexes can be +ve or -ve 
a = 'SATARA'
a[0:4] # SATA
a[0:-3] # SATA
b = len(a)
a[0:b:2] # STR

# string function / methods
len(a) # to find the length of string
a.endswith('A') # to check whether the string ends with following seq. or not
a.count('A') # to find the count of input character / sequence in the string
a.capitalize() # to return string with first letter as capital
a.find('A') # finds the word in the string and returns its index
a.replace('A','a') # method to replace all with parameter string seq.