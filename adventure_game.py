## mr joo developer website
import time

def intro():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark and mysterious forest.")
    time.sleep(2)
    print("You have two paths ahead of you. Will you go left or right?")

def left_path():
    print("You chose the left path.")
    time.sleep(1)
    print("As you venture deeper, you come across a river.")
    time.sleep(2)
    print("Do you try to swim across or look for a bridge?")

def right_path():
    print("You chose the right path.")
    time.sleep(1)
    print("The path leads you to a cave entrance.")
    time.sleep(2)
    print("Will you enter the cave or continue on the path?")

def swim_or_bridge():
    print("You decided to swim across the river.")
    time.sleep(1)
    print("The current is strong, and you're swept away!")
    time.sleep(2)
    print("Game Over.")

def cave_or_continue():
    print("You entered the cave cautiously.")
    time.sleep(1)
    print("Inside the cave, you find a treasure chest!")
    time.sleep(2)
    print("Congratulations, you've won the game!")

def continue_on_path():
    print("You continue on the path.")
    time.sleep(1)
    print("Suddenly, you encounter a group of wild animals!")
    time.sleep(2)
    print("You try to run, but it's too late.")
    time.sleep(2)
    print("Game Over.")

def main():
    intro()

    user_choice = input("Left or right? ").lower()

    if user_choice == "left":
        left_path()
        choice = input("Swim or bridge? ").lower()
        if choice == "swim":
            swim_or_bridge()
        elif choice == "bridge":
            print("You found a bridge and crossed safely.")
            cave_or_continue()
        else:
            print("Invalid choice.")
    elif user_choice == "right":
        right_path()
        choice = input("Cave or continue? ").lower()
        if choice == "cave":
            cave_or_continue()
        elif choice == "continue":
            continue_on_path()
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
