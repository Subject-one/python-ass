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
    print("We are building a meal manually")

# Random Option Dinner Plan
def dp_rand():
    print("We are building a meal at random")

# User option
def user_option():
    input("Manual or Random Dinner Plan Builder?(manual/random): ")
    if user_option != "random" or "manual":
        input("You need to specify 'manual' or 'random': ")
    elif user_option == "manual":
        dp_man()
    elif user_option == "random":
        dp_rand()
        