import math
def reverse_array(arr):
    for i in range(math.floor(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr

array =  ["a", "b", "c", "d", "e"]

print(reverse_array(array))