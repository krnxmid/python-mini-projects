# BLACK JACK GAME IN PYTHON

import random
import os
import sys

ascii_art = r'''
 _     _            _    _            _               _____                 
| |   | |          | |  (_)          | |             |A .  | _____         
| |__ | | __ _  ___| | ___  __ _  ___| | __          | /.\ ||A ^  | _____   
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /          |(_._)|| / \ ||A _  | _____
| |_) | | (_| | (__|   <| | (_| | (__|   <           |  |  || \ / || ( ) ||A_ _ |
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\          |____V||  .  ||(_'_)||( v )|
                       _/ |                                 |____V||  |  || \ / |     
                      |__/                                         |____V||  .  |     
                                                                          |____V|       
'''
print(ascii_art)
play_or_not = input("Do you want to play a game of blackjack? 'y' to play: ").lower()

if play_or_not != "y":
    print("Goodbye!")
    sys.exit()
os.system("cls")

dealer_cards = []
player_cards = []

dealer_wins = False
player_wins = False
        
def generate_cards():
    dealer_cards.extend([random.randint(2,11), random.randint(2,11)])
    player_cards.extend([random.randint(2,11), random.randint(2,11)])
    return dealer_cards, player_cards

def show_score(dealer_cards, player_cards):
    print(f"Your Cards: {player_cards}. Current score: {sum(player_cards)}")
    print(f"Dealer's Cards: [{dealer_cards[0]}, ?]")
    
def hit_or_not(dealer_cards, player_cards):
    choice = input("Do you want to hit or not 'y' or 'n': ").lower()
    
    if choice == "y":
        player_cards.append(random.randint(2,11))
        show_score(dealer_cards=dealer_cards, player_cards=player_cards)
        return True
    elif choice == "n":
        return False
    else:
        os.system("cls")
        print("Enter 'y' or 'n'")

def dealer_turn(dealer_cards):
        dealer_cards.append(random.randint(2,11))
        show_score(dealer_cards=dealer_cards, player_cards=player_cards)
        
        while sum(dealer_cards) < 17:
            dealer_cards.append(random.randint(2,11))
        print(f"Dealer draws another card. Dealer's cards: {dealer_cards}. Current Score: {sum(dealer_cards)}")
        
        return dealer_cards

def blackjack(dealer_score, player_score):
    os.system("cls")
    
    if player_score > 21:
        print("You lose, You went over 21!")
        dealer_wins = True
    elif dealer_score > 21:
        player_wins = True
        print("You win, dealer went over 21!"  )
    else:
        if player_score > dealer_score:
            player_wins = True
            print("You win!")
        elif dealer_score > player_score:
            dealer_wins = True
            print("You lose!")
        else:
            dealer_wins = True
            player_wins = True
            print("Its a Draw/Push!")

generate_cards()
show_score(dealer_cards=dealer_cards, player_cards=player_cards)

while sum(player_cards) <= 21:
    if hit_or_not(dealer_cards, player_cards) == False:
        break

if sum(player_cards) <= 21:
    dealer_cards = dealer_turn(dealer_cards=dealer_cards)

blackjack(dealer_score=sum(dealer_cards), player_score=sum(player_cards))