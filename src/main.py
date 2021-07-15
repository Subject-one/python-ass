import os
from sys import argv
from datetime import datetime
from functions import dp_man, lets_go, total_cost, total_calories, total_carbs, total_fat, total_protein, total_serve, show_choices, get_choice, exit_prog
from items import sides

today = datetime.now()
print(today.strftime("Date: %a, %d %B, %y"))
print(today.strftime("Time: %I:%M:%S %p"))

lets_go()

dp_man()

# print(sides)





