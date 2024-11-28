import random
import os


HANGMANPICS = [
    r"""  
  +---+ 
      | 
      | 
      | 
      | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========""",
    
    r"""  
  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
========="""
]

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


######### Start #########

random_word = random.choice(words)
blank_word = '_' * len(random_word)
print("########## Welcome to Hangman! ##########")
print(" ")
print(f"The word is {blank_word}")
print(" ")
# print(random_word)


def hangman():
    game_over = False

    correct_letters = []

    incorrect_guess = 0
    
    while not game_over:

        display_word = ""
        # print(f"The word is {display_word}")
        print(" ")
        user_guess = input("Enter your guess: ")

        os.system("cls")

        correct_guess = False

        for letter in random_word:
            if letter == user_guess:
               display_word += user_guess
               correct_letters.append(letter)
               correct_guess = True

            elif letter in correct_letters:
                display_word += letter

            else:
               display_word += "_"

        if correct_guess is not True:
            incorrect_guess += 1
            # print(f"({6-incorrect_guess}/6) lives remaining")

        if incorrect_guess == 6:
            print("You have lost!")
            print(HANGMANPICS[incorrect_guess])
            print(f"The word was {random_word}!")
            break

        print(f"Word is {display_word}")

        if "_" not in display_word:
            print(" ")
            print("########## You have won the game! ##########")
            game_over = True
            break
      
        print(" ")
        print(f"({6-incorrect_guess}/6) lives remaining")
        print(HANGMANPICS[incorrect_guess])
        input("Press any key to continue...")
        os.system("cls")


hangman()