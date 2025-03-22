# py code to find 2nd largest in the array.
def secondLarge(arr):
    arr.sort()
    return arr[len(arr)-2]
print(secondLarge([10, 5, 8, 20, 15]))