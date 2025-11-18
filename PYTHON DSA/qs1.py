#Reverse a list without using reverse() or [::-1]
arr = [1,2,3,4]
def reverse_list(arr):
    """ this function will reverse the list"""

    left , right = 0, len(arr)-1
    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -=1
    return arr
    print(arr)
