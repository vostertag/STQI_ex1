



def checkSorting(array):
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            print("The array is not sorted correctly")
            return False
    
    return True

