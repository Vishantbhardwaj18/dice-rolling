import random

def roll_dice():
    return random.randint(1, 6)

def dice_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        user_input = input("Roll the dice? (yes/no): ").lower()
        if user_input == "yes":
            result = roll_dice()
            print(f"You rolled a {result}")
        elif user_input == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    dice_simulator()
