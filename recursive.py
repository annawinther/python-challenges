def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n - 1)

# recursive search function
def recursvie_search(arr, target):
    for i in arr:
        if len(arr) == 0:
            return 1
        elif target == i:
            return True
    return False

arr = []
yo = recursvie_search(arr, 2)
print(yo)