from sys import set_asyncgen_hooks
from items import mains, sides, sauces, drinks
from simple_term_menu import TerminalMenu


# Start application
def lets_go():
    print("""Welcome to the Meal Planner.
    Follow the prompts to build your meal.
    You can stop running this program by typing 'exit' at any point.
    Type -help for addtional information.""")
    input("Press Enter to Build Your Meal...")
    if (" "):
        print("Let's plan!")

# Manual Option For Dinner Plan
def dp_man():
    print("Manual Mode. Let's Build!")
    main_c = [*mains.keys()]
    # print(main_c)
    user_choice = show_choices(main_c, "main")
    print(user_choice)
    if user_choice == "Steak":
        steak_choice = get_choice("Steak")
        print(steak_choice)

def show_choices(choice_list, menu):
    for counter, choice in enumerate(choice_list, 1):
        print(f"{counter}. {choice}")
    print("Q. Quit")
    user_choice = input(f"Choose {menu}")
    if user_choice.upper() == "Q" or user_choice.lower() == "quit":
        exit_prog()
    return user_choice

def get_choice(choice):
    return show_choices([*mains[f"{choice}"].keys()], f"{choice}")

def exit_prog():
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