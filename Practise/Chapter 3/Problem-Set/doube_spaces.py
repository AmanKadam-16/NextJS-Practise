try:
    print('Double space detector')
    ans = input('Enter valid sentence..')
    print(f'Your input sentence contains {ans.replace('  ','_').count('_')} double spaces')
    print(f''' 
Following is your formatted sentence:
        =>  {ans.replace('  ',' ')} 
''')
except Exception as e:
    print('Some error occured.')