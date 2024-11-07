import random
import os

# ASCII arts for rock, paper, and scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Main logic function
def program():
    try:
        user_choice = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
        if user_choice not in [1, 2, 3]:
            print("Please enter a value from 1 to 3!")
            return

        computer_choice = random.randint(1, 3)
        game_images = ["Rock", "Paper", "Scissors"]

        # Print choices
        print(f"You chose: {game_images[user_choice - 1]}")
        print(f"Computer chose: {game_images[computer_choice - 1]}")

        # Determine the result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print("You win!")
        else:
            print("You lose!")

        # Display ASCII art
        if computer_choice == 1:
            print(rock)
        elif computer_choice == 2:
            print(paper)
        elif computer_choice == 3:
            print(scissors)

    except ValueError:
        print("Invalid input! Please enter a number from 1 to 3.")

# Main loop
while True:
    program()
    input("Press Enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")
