#function finds the second largest number in a list without sorting.

arr  = [2,3,8,5]

def second_largest(arr):
    """this function with find the second largest number in the list"""
    first = second = float['-inf']
    for x in arr:
        if x > first:
           second = first
           first = x
        elif x > second and x != first:
            second = x
    return arr