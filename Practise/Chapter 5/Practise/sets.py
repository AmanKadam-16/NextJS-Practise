# the sets are denoted inside {} and they are immutable and items are unique and non-repetitive
# Following are some operations on sets()
s1 = {1,2,3,4,5}
len(s1) # by using len() w`e can find the length of the set{}
s1.remove(5) # removes the passed item if exists in the set{}
s1.pop() # this method removes the first element from the set{}
s1.clear() # clears the set and makes it empty set{}
s1.union({3,4,5,2,9}) # In this we're going to merge two sets by union()
s1.inptersection({1,55,3})  # this mehthod finds common items in both sets and return them.