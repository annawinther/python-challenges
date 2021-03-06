# Challenge: Classify the runtime of each function

import math
n = 100 # size of 100  --> O(1)

# 1
def foo(n):
  sq_root = int(math.sqrt(n)) # O(1)
  for i in range(0, sq_root): # O(n) * O(1)
    print(i) # O(1)

# O(1) + O(1) + O(n) * 1 + O(1) 
# = O(3) +  O(n)
# = O(n) is the runtime --> 
# This has a linear runtime

# 2
def bar(x):
  sum = 0                   # O(1)
  for i in range(0, 1463): #O(1)
    i += sum                # O(1)
    for j in range(0, x):   # O(n)
      for k in range(x, x + 15): # O(1)
        sum += 1                 # O(1)

# = O(n) Linear

print(bar(100))

# prints: none

# 3 
array = [1, 3, 4, 2, 6]

def baz(array):
  print(array[1])
  midpoint = len(array) // 2 # O(1)
  for i in range(0, midpoint): # O(n) * O(1)
    print(array[i]) # O(1)
  for _ in range(1000): # O(1)
    # pass
    print('hi') # O(1)

# O(1) + O(1) + O(n) * 1 + O(1) + (1) = O(n)
# This is a linear
