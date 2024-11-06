import random, time, os

def passgen():
    # all the capital, lowercase, numbers, special characters for generating password
    capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = [element.lower() for element in capital]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]

    # combining all the lists to make one list
    combined = list(capital + lowercase + number + special_characters)

    # shuffle the contents of the combined list
    random.shuffle(combined:10) # you can change teh "10" to get any amount of characters

    # the final clean output without the brackets and commas
    clean_output = ''.join(str(element) for element in combined)
    print(clean_output)
    
    
while True:
    time.sleep(0.1)
    os.system("cls")
    passgen()
  
