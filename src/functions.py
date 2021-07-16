import os
from time import sleep
from items import mains, sides, sauces, drinks
from simple_term_menu import TerminalMenu
import random

# Nice to have (if time permits): 
# Take-away menu
# y/n do you want to restart dp_man()

# Start application
def lets_go():
    os.system("clear")
    print("|=========================================|")
    print("|      PLEASE READ BEFORE CONTINUING!     |")
    print("|=========================================|\n")
    print("""Welcome to the Meal Planner.
Follow the prompts to build your meal.\n
! You must use the arrow keys to navigate.\n
! Type -help for additional information.\n
! Type -q to quit the application.\n""")
    sleep(2)

# Set Username / Exit Program
def set_user():
    user_name = input("Enter a command(-help, -q) OR Enter your name to start:\n")
    if user_name == "-Q":
        exit_prog()
    elif user_name == "-q":
        exit_prog()
    else:
        print(f"\nYou look great today, {user_name}.\nLet's Build a Meal together!\n")
    sleep(1)

# Option Selector 
def user_selector():
    user_option = input("Manual or Random Dinner Plan Builder?(manual/random):\n")
    if user_option == "random":
        dp_rand()
    elif user_option == "Random":
        dp_rand()
    elif user_option == "manual":
        dp_man()
    elif user_option == "Manual":
        dp_man()
    elif user_option == "-Q":
        exit_prog()
    elif user_option == "-q":
        exit_prog()
    else:
        print("You didn't specifiy 'random or manual'")
        return user_option 

# Random Option Dinner Plan
def dp_rand():
    item_selection = []
    menu_selection = []

    main_c = [*mains.keys()]
    r_choice = random.choice(main_c)
    menu_selection.append(r_choice)
    r_list = [*mains[f"{r_choice}"].keys()]
    r_choice = random.choice(r_list)
    item_selection.append(r_choice)

    sides_c = [*sides.keys()]
    r_choice = random.choice(sides_c)
    menu_selection.append(r_choice)
    r_list = [*sides[f"{r_choice}"].keys()]
    r_choice = random.choice(r_list)
    item_selection.append(r_choice)

    sauces_c = [*sauces.keys()]
    r_choice = random.choice(sauces_c)
    menu_selection.append(r_choice)
    r_list = [*sauces[f"{r_choice}"].keys()]
    r_choice = random.choice(r_list)
    item_selection.append(r_choice)

    drinks_c = [*drinks.keys()]
    r_choice = random.choice(drinks_c)
    menu_selection.append(r_choice)
    r_list = [*drinks[f"{r_choice}"].keys()]
    r_choice = random.choice(r_list)
    item_selection.append(r_choice)

    print(item_selection)
    print("Total Cost:$", total_cost(menu_selection, item_selection))
    print("Total Carbs: ", total_carbs(menu_selection, item_selection),"(g)")
    print("Total Protein: ", total_protein(menu_selection, item_selection),"(g)")
    print("Total Calories: ", total_calories(menu_selection, item_selection), "(cal)")
    print("Total Serving Size: ", total_serve(menu_selection, item_selection), "(g)")

# Dinner Plan Manual
def dp_man():
    print("Now Loading...\n")
    sleep(1)
    print("|==========================================|")
    print("|          Launching Manual Mode           |")
    print("|==========================================|")
    sleep(2)

    item_selection = []
    menu_selection = []

    # Selecting Mains
    main_c = [*mains.keys()]
    main_c.append("Quit")
    user_choice = show_choices(main_c, "Please choose a Main Dish")
    if user_choice == "Steak":
        menu_selection.append("Steak")
        item_selection.append(get_choice("Steak", mains))
        main_c = [*mains.keys()]
    elif user_choice == "Chicken":
        menu_selection.append("Chicken")
        item_selection.append(get_choice("Chicken", mains))
    elif user_choice == "Fish":
        menu_selection.append("Fish")
        item_selection.append(get_choice("Fish", mains))
    elif user_choice == "Tofu":
        menu_selection.append("Tofu")
        item_selection.append(get_choice("Tofu", mains))
    
    # Selecting Sides
    sides_c = [*sides.keys()]
    sides_c.append("Quit")
    user_choice = show_choices(sides_c, "Please choose a Side Dish")
    if user_choice == "Potato":
        menu_selection.append("Potato")
        item_selection.append(get_choice("Potato", sides))
    elif user_choice == "Healthy Vegetables":
        menu_selection.append("Healthy Vegetables")
        item_selection.append(get_choice("Healthy Vegetables", sides))
    
    # Selecting Sauces
    sauces_c = [*sauces.keys()]
    sauces_c.append("Quit")
    user_choice = show_choices(sauces_c, "Please choose a sauce")
    if user_choice == "Creamy":
        menu_selection.append("Creamy")
        item_selection.append(get_choice("Creamy", sauces))
    elif user_choice == "Savory":
        menu_selection.append("Savory")
        item_selection.append(get_choice("Savory", sauces))

    # Selecting Drinks
    drinks_c = [*drinks.keys()]
    drinks_c.append("Quit")
    user_choice = show_choices(drinks_c, "Please choose a drink")
    if user_choice == "Soft Drink":
        menu_selection.append("Soft Drink")
        item_selection.append(get_choice("Soft Drink", drinks))
    elif user_choice == "Healthy Option":
        menu_selection.append("Healthy Option")
        item_selection.append(get_choice("Healthy Option", drinks))

    # print(menu_selection)
    print("The Dinner Plan for tonight is: ")
    print(item_selection)
    # print(mains[menu_selection[0]][item_selection[0]]["Price"])
    # print(sides[menu_selection[1]][item_selection[1]]["Price"])
    print("Total Cost: $", total_cost(menu_selection, item_selection))
    print("Total Carbs: ", total_carbs(menu_selection, item_selection),"(g)")
    print("Total Protein: ", total_protein(menu_selection, item_selection),"(g)")
    print("Total Calories: ", total_calories(menu_selection, item_selection), "(cal)")
    print("Total Serving Size: ", total_serve(menu_selection, item_selection), "(g)")

# Total cost of all items in the meal
def total_cost(menu_selection, item_selection):
    dict_list = [mains, sides, sauces, drinks]
    price_list = []
    for index, menu in enumerate(dict_list):
        price_list.append(menu[menu_selection[index]][item_selection[index]]["Price"])
    return sum(price_list)

# Total carbs of all items in the meal
def total_carbs(menu_selection, item_selection):
    dict_list = [mains, sides, sauces, drinks]
    carb_list = []
    for index, menu in enumerate(dict_list):
        carb_list.append(menu[menu_selection[index]][item_selection[index]]["Carbs(g)"])
    return sum(carb_list)

# Total protein of all items in the meal
def total_protein(menu_selection, item_selection):
    dict_list = [mains, sides, sauces]
    protein_list = []
    for index, menu in enumerate(dict_list):
        protein_list.append(menu[menu_selection[index]][item_selection[index]]["Protein(g)"])
    return sum(protein_list)

# Total fat of all items in the meal
def total_fat(menu_selection, item_selection):
    dict_list = [mains, sides, sauces, drinks]
    fat_list = []
    for index, menu in enumerate(dict_list):
        fat_list.append(menu[menu_selection[index]][item_selection[index]]["Fat(g)"])
    return sum(fat_list)

# Total calories of all items in the meal
def total_calories(menu_selection, item_selection):
    dict_list = [mains, sides, sauces, drinks]
    calories_list = []
    for index, menu in enumerate(dict_list):
        calories_list.append(menu[menu_selection[index]][item_selection[index]]["Calories"])
    return sum(calories_list)

# Total serving size of all items in the meal
def total_serve(menu_selection, item_selection):
    dict_list = [mains, sides, sauces]
    serve_list = []
    for index, menu in enumerate(dict_list):
        serve_list.append(menu[menu_selection[index]][item_selection[index]]["Serving Size(g)"])
    return sum(serve_list)
   
# Arrow list choice selector
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

# Shows which list
def get_choice(choice, menu):
    choice_list = [*menu[f"{choice}"].keys()]
    choice_list.append("Quit")
    return show_choices(choice_list, f"{choice}")

# Exit Message when 'Quit' selected. Clears terminal
def exit_prog():
    print(f"See you again soon!\nNow Closing App...")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    os.system("clear")
    exit()
    







