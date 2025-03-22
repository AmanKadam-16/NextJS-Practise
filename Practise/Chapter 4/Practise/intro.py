# Now in this chapter we're going to learn about advance datatypes in Python.
# in python we can store data of multiple or same data types in various types of containers
# they are List [] , tuple (), dictionary {}

# A List can be defined by
list1 = ['anyString', 3, False, -7]
# Even accessing list is pretty easy
list1[3:] # from index 3 till last index. similar to string 

# Here are some list methods available in python
# 1. Sorting a List with sort() method
demoList = [3,1,5,4,6,7,4]
demoList.sort()

# 2. reversing a List with reverse() method
demoList.reverse()

# 3. adding an item to the end of list with append() method
demoList.append(90)

# 4. insert an item to a specific index with insert() method
demoList.insert(4, 23) # here we insert number 23 to the 4th index

# 5. to remove an item from the list and return its index we use pop() method
demoList.pop(3) # 3rd index item would be deleted

# 6. directly remove an item from the list by its name we use remove() method
demoList.remove(90)


# Now we're moving towards tuples in Python | they are enclosed into ()
# But one important thing to note is that once tuple is defined
# its elements cannot be altered or manipulated.
# so as per college definitions we can say that a list is mutable 
# but a tuple is immutable 
demoTuple = (3,'anyString',False, -4)

# And following are some of the tuple methods in Python
demoTuple.count('anyString') # This method is used to find count of item in the tuple
demoTuple.index(3) # This will return the index 
# at which the passed element is present if not then it raises valueError | index()

