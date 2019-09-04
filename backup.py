import shutil
import os


def optionOne():
    print("You selected option one")

def optionTwo():
    print("You selected option Two")


def main():
    userInput = False
    while userInput == False:
        option = input("Backup Options: \n 1: Full backup \n 2: Game Play \n Select An Option: ")
        if option == 1:
            optionOne()
            userInput = True
        elif option == 2:
            optionTwo()
            userInput = True
        else:
            print("Invalid input")
            userInput = False


main()