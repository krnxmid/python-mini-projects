import random

number = random.randint(1,101)
print("Welcome to Guess the Number!")
attempts = None

def game_difficulty():
    '''Set the difficulty for the game'''
    global attempts
    
    print("Choose the difficulty of the game!")
    
    print(" ")
    attempts = 0
    
    while True:
        difficulty = int(input("Enter 1 for easy, 2 for hard: "))

        if difficulty == 1:
            attempts = 10
            break
        elif difficulty == 2:
            attempts = 5
            break
        else:
            print("Enter '1' or '2'")
        
    return attempts


def guess_the_number(attempts, number):
    '''Main game for guessing the number'''
    
    wrong_guesses = 0
    
    for i in range(0, attempts):
        print(" ")
        guess = int(input("Enter your guess (1-100): "))
        
        if guess > number:
            print("You went over the number!")
        elif guess < number:
            print("Your guess is less than the number.")
        
        if guess != number:
            wrong_guesses += 1
            print(f"You have {attempts-wrong_guesses} attempts left!")
            # print(number)
        else:
            print("You have guessed the number!")
            break
        
        print(" ")
        
        if wrong_guesses == attempts:
            print("You lose!")
            print(f"The number was {number}")
            break

game_difficulty()
guess_the_number(attempts=attempts, number=number)
