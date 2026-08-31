#Way 1: to import directly which function to use
from functions import square
for i in range(10):
  print(f"The square of {i} is {square(i)}")

#Way 2: import whole functions.py file

import functions
for i in range(10):
  print(f"The square of {i} is {functions.square(i)}")