import os
from sys import argv
from datetime import datetime
from functions import dp_man, dp_rand, lets_go, set_user, user_selector

print(argv)
if "--random" in argv:
    dp_rand()
    exit()

today = datetime.now()
print(today.strftime("Date: %a, %d %B, %y"))
print(today.strftime("Time: %I:%M:%S %p"))

lets_go()
set_user()
user_selector()
#dp_rand()
# print(sides)
