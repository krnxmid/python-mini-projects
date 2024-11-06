
#   TEXT WAVE GENERATOR. MADE BY KARAN

#Import os for the cls command time for the time.sleep delay
import os, time

#The word which will be animated
word = input("Enter your word: ")

#length of the word
wordlen = len(word)

#Main program which is looped
while True:
    #Main animation process
    for index in range(wordlen):

        #The uppercase word:
        mod_word = word[:index].lower() + word[index].upper() + word[index+1:]

        #Print the word
        print(mod_word)

        #delay of 3 miliseconds
        time.sleep(0.3)

        #The 'cls; command so that it automatically clears the previous text
        os.system('cls' if os.name == 'nt' else "printf '\033c'")

        #Cycling through all the letters again and again
        index += 1
    
