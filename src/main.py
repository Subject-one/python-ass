import os
from sys import argv
from datetime import datetime
from functions import dp_man, lets_go, set_user

today = datetime.now()
print(today.strftime("Date: %a, %d %B, %y"))
print(today.strftime("Time: %I:%M:%S %p"))

lets_go()
set_user()
dp_man()

# print(sides)