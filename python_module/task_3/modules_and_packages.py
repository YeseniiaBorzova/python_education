
"""Working with python packages"""

import re


string = sorted(dir(re))
functions = [s for s in string if "find" in s]
print(functions)
