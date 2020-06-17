# Linear Sorting
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1  #not found

# result = linear_search(array, 5)
# print(result)

# Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = int((low+high)/2)
        # print(middle)
        if target < arr[middle]:
            high = middle-1
        elif target > arr[middle]:
            low = middle+1
        else:
            return middle
    return -1 #not found

result = binary_search(array, 5)
print(result)