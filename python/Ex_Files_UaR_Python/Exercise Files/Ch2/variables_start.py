# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# ERROR: variables of different types cannot be combined
from datetime import date
from datetime import time
from datetime import datetime

  ## DATE OBJECTS
# print out the date's individual components
now = datetime.now()
# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print (now.strftime("%I:%M:%S %p")) # 12-Hour:Minute:Second:AM
print (now.strftime("%H:%M")) # 24-Hour:Minute