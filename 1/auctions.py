import os

bids = {}

gavel = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                        / '-------'`\\
                       .-------------.
                      /_______________\\
'''

def auction():
    print(gavel)
    print("####################### BLIND AUCTION ####################### ")
    while True:
        name = input("Enter your name: ")
        amount = int(input("Enter teh amount of bid: $"))
        bids[name] = amount

        os.system("cls")
        choice = input("Are there another person? (y/n): ").lower()
        os.system("cls")
        if choice == "y":
            continue
        elif choice == "n":
            sorted_dict = dict(sorted(bids.items()))
            
        winner = 0    
        print("########## RESULTS ##########")
        for key, value in sorted_dict.items():
            if winner == 0:
                print(gavel)
                print(" ")
                print(f"Winner is {key} with a bid of {value}!")
                print(" ")
                winner += 1
            else:
                print(f"{key}: {value}")                
        
auction()