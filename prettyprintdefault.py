from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string, 
# Python comments or blank lines before the __future__ line.
import pprint
import numpy as np
def print(*args, **kwargs):
    """My custom print() function."""
    return pprint.pprint(*args, **kwargs)

a=np.ones((10,10))
print("Hi Mike") 
print(a)
