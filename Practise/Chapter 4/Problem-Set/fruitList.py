# Python Program to take 7 fruits from user and store it in a List | []
fruitsList = []
for i in range(7):
    fruitName = input(f'Enter fruit name {i} : ')
    fruitsList.append(fruitName)
print('Following are the fruits in your cart : ',fruitsList)