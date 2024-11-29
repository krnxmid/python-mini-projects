def get_input():
    word = input("Enter your word: ")
    word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shift_amount = int(input("Enter shift amount: "))
    return word, word_list, shift_amount

def encode(word, word_list, shift_amount):
    for i in range(len(word)):
        # Check if the character is a space, print it directly
        if word[i] == ' ':
            print(' ', end='')
        else:
            letter_index = word_list.index(word[i])
            final_index = letter_index + shift_amount
            final_index = final_index % len(word_list)
            print(word_list[final_index], end='')

def decode(word, word_list, shift_amount):
    for i in range(len(word)):
        # Check if the character is a space, print it directly
        if word[i] == ' ':
            print(' ', end='')
        else:
            letter_index = word_list.index(word[i])
            final_index = letter_index - shift_amount
            final_index = final_index % len(word_list)
            print(word_list[final_index], end='')

def logo():
    logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
    print(logo)

def main():
    logo()
    print("######################## ENCODE / DECODE ########################")
    print(" ")
    word, word_list, shift_amount = get_input()  # Capture the input after the logo is printed

    encode_or_decode = input("Would you like to encode or decode? (e/d): ")

    if encode_or_decode.lower() == 'e':
        encode(word, word_list, shift_amount)
    elif encode_or_decode.lower() == 'd':
        decode(word, word_list, shift_amount)
    else:
        print("Invalid choice.")

# Call the main function to start the program
main()
