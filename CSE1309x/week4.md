Loops, Nested Loops, Functions & Modules
Loops & Nested Loops
 - two types, for and while
 while <statement>; [colon]
 tab = 4 spaces
 Babylonian
 while True - beware the infinite loop.
Functions
Modules (ie from x import y)
 first my_math.py file has
 def add_number(x,y):
     return x+y
 def multiply_numbers(x,y)
     return x*y
second .py
import my_math  # {note: drop the .py extension}
a=5
b=8
c=my_math.add_numbers(a,b)
print c
d=my_math.multiply_numbers(a,b)
print d
then to save a bit of time, make tidier, change the import statement
from "import my_math" to "from my_math import add_numbers , multiply_numbers"
or just "from my_math import *"
then you can remove the prefix "my_math."
remember eg "import math" means you still need to explicitly call the imported function ie math.sqrt
BUT if you used "from math import *" then the function becomes sqrt(x)
for futher readin on all the python 'standard' modules visit http://docs.python.org/3/py-modindex.html
