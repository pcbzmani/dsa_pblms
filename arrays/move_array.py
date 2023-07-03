def move_zeros(arr):
    '''
    INPUT arr is a simple Python list
    Don't return anything, modify arr in place.
    The solution code will just check on the current state of arr.
    For example:
    arr = [1,2,3] inside the function and then don't return anything.
    '''
    j = 0
    for i in arr:
        if i != 0:
            arr[j] = i
            j += 1 
    
    arr[j:] = [0] * (len(arr) - j)
