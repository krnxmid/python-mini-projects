import time
import os

capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = [element.lower() for element in capital]
text = input("Enter your text: ")

for index, char in enumerate(text):
    index = 0
    
    while True:
        if str(char) == lower[index]:
            time.sleep(0.2)
            break
        elif str(char) != lower[index]:
            time.sleep(0.2)
            print(lower[index], end='\r')
        index += 1
        
    print(char)
