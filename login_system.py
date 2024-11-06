# A SIMPLE SING UP AND SIGN IN SYSTEM!!!!!
# Feel free to use it!
# Made by KARANVEER SINGH


# Import neccessary modules
import os
import time

# Sign up function
def signup():
    os.system("cls")

    ######### Main Menu #########
    print(" ")
    print("-----------------")
    print("#### Sign Up ####")
    print("-----------------")
    print(" ")

    username = input("Enter your username: ")
    print(" ")

    password = input("Enter your password: ")
    os.system("cls")

    ######### Outcome ##########
    print("Sign up Successful")
    print(" ")
    input("Press any key to continue...")
    os.system("cls")

    return username, password

# Sign in function
def signin(user1, pass1):
    os.system("cls")

    ######### Main Menu #########
    print(" ")
    print("-----------------")
    print("#### Sign In ####")
    print("-----------------")
    print(" ")

    username = input("Enter your username: ")
    print(" ")
    password = input("Enter your password: ")


    ######### Outcome ##########
    if username == user1 and password == pass1:
        os.system("cls")
        print("Login successful!")
        print(" ")
        input("Press any key to continue...")
        os.system("cls")
    else:
        os.system("cls")
        print("Login unsuccessful!, username or password not found")
        print(" ")
        input("Press any key to continue...")
        os.system("cls")

# Main Menu
def menu():

    username = None
    password = None

    ######### Main Menu #########
    while True:
        os.system("cls")
        print("#### Sign up & Sign in ####")
        print(" ")
        print("-------------")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        print("-------------")
        print(" ")

        choice = input("Enter your choice: ")

    ######### Outcome ##########
        if choice == "1":
            username, password = signup()
        elif choice == "2":
            signin(user1 = username, pass1 = password)
        elif choice == "3":
            os.system("cls")
            os.system("exit")
            break
        else:
            os.system("cls")
            print("Enter 1, 2, 3 please!")
            print(" ")
            input("Press any key to continue...")
            
menu()
