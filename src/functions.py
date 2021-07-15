import os
from time import sleep
from items import mains, sides, sauces, drinks
from simple_term_menu import TerminalMenu

# Take away option

#Add note for CRTL-C quit
# Start application
def lets_go():
    user_name = []
    print("""Welcome to the Meal Planner.
    Follow the prompts to build your meal.
    You can stop running this program by typing 'exit' at any point.
    Type -help for addtional information.""")
    try:
        input("Enter your name to proceed: ")
    except ValueError:
        input("Put some letters in bro: ")
    
    
# Manual Option For Dinner Plan
def dp_man(): 
    item_selection = []
    menu_selection = []
    print("Manual Mode. Let's Build!")
    main_c = [*mains.keys()]
    main_c.append("quit")
    user_choice = show_choices(main_c, "Please choose a Main Dish")
    if user_choice == "Steak":
        menu_selection.append("Steak")
        item_selection.append(get_choice("Steak", mains))
    # print(item_selection)
    # elif user_choice == "Chicken":
    sides_c = [*sides.keys()]
    sides_c.append("quit")
    user_choice = show_choices(sides_c, "Please choose a Side Dish")
    if user_choice == "Potato":
        menu_selection.append("Potato")
        item_selection.append(get_choice("Potato", sides))
    # print(item_selection)
    # y/n do you want to restart dp_man()
    print(menu_selection)
    print(item_selection)
    # print(mains[menu_selection[0]][item_selection[0]]["Price"])
    # print(sides[menu_selection[1]][item_selection[1]]["Price"])
    print(total_cost(menu_selection, item_selection))
    print(total_carbs(menu_selection, item_selection))

def total_cost(menu_selection, item_selection):
    dict_list = [mains, sides]
    price_list = []
    for index, menu in enumerate(dict_list):
        price_list.append(menu[menu_selection[index]][item_selection[index]]["Price"])
    return sum(price_list)

def total_carbs(menu_selection, item_selection):
    dict_list = [mains, sides]
    carb_list = []
    for index, menu in enumerate(dict_list):
        carb_list.append(menu[menu_selection[index]][item_selection[index]]["Carbs(g)"])
    return sum(carb_list)

def total_protein(menu_selection, item_selection):
    dict_list = [mains, sides]
    protein_list = []
    for index, menu in enumerate(dict_list):
        protein_list.append(menu[menu_selection[index]][item_selection[index]]["Protein(g)"])
    return sum(protein_list)

def total_fat(menu_selection, item_selection):
    dict_list = [mains, sides]
    fat_list = []
    for index, menu in enumerate(dict_list):
        fat_list.append(menu[menu_selection[index]][item_selection[index]]["Fat(g)"])
    return sum(fat_list)

def total_calories(menu_selection, item_selection):
    dict_list = [mains, sides]
    calories_list = []
    for index, menu in enumerate(dict_list):
        calories_list.append(menu[menu_selection[index]][item_selection[index]]["Calories(g)"])
    return sum(calories_list)

def total_serve(menu_selection, item_selection):
    dict_list = [mains, sides]
    serve_list = []
    for index, menu in enumerate(dict_list):
        serve_list.append(menu[menu_selection[index]][item_selection[index]]["Serving Size(g)"])
    return sum(serve_list)
   


def show_choices(choice_list, menu):
    os.system("clear")
    try:
        terminal_menu = TerminalMenu(choice_list, title=menu)
        user_choice = terminal_menu.show()
        last_option = len(choice_list)-1
        if user_choice == last_option:
            exit_prog()
        return choice_list[user_choice]
    except TypeError:
        exit_prog()

def get_choice(choice, menu):
    choice_list = [*menu[f"{choice}"].keys()]
    choice_list.append("quit")
    return show_choices(choice_list, f"{choice}")

def exit_prog():
    print("Thanks for using my shit")
    sleep(2)
    os.system("clear")
    exit()
    







# Random Option Dinner Plan
# def dp_rand():
#     print("Generating a randomised meal plan...")

# User option
# def user_option():
#     input("Manual or Random Dinner Plan Builder?(manual/random): ")
#     if user_option != "random" or "manual":
#         input("You need to specify 'manual' or 'random': ")
#         return
#     elif user_option == "manual":
#         dp_man()
#     elif user_option == "random":
#         dp_rand()