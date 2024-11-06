import random, os

# Ascii arts for rack, paper and scissors

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

# Main logic:

def program():
    
    user_choice = int(input("Enter 1 for rock, 2 for paper or 3 for scissors: "))
    computer_choice = random.randint(1,3)
    
    game_images = ["Rock", "Paper", "Scissors"]
    
    if user_choice > 3:
        print("Enter a value from 0 to 2!")
    elif user_choice == computer_choice:
        print(f"Its a Tie! computer also chose {game_images[computer_choice - 1]}")
    elif (user_choice == 1 and computer_choice == 3) or \
        (user_choice == 2 and computer_choice == 1) or \
        (user_choice == 3 and computer_choice == 2):
        print(f"You win!, computer chose {game_images[computer_choice - 1]}")
    else:
        print(f"You lose!, computer chose {game_images[computer_choice - 1]}")
    
        
while True:
    program()
    input("Press enter to continue...")
    os.system("cls")
