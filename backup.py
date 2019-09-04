import shutil
import os


def documentBackup():
    print("You selected document backup")

def pictureBackup():
    print("You selected picture backup")

def videoBackup():
    print("You selected video backup")

def xamppBackup():
    print("You selected xampp backup")

def completeBackup():
    print("You selected complete backup")

def csBackup():
    print("You selected Counter Strike backup")

def d2Backup():
    print("You selected Destiny 2 backup")

def nmsBackup():
    print("You selected No mans sky backup")

def pubgBackup():
    print("You selected pubg backup")

def main():
    userInput = False
    while userInput == False:
        option = input("Backup Options: \n 1: Dcouments \n 2: Pictures \n 3: Videos \n 4: Xampp \n 5: Complete Backup \n 6: Game Play \n ---------------------- \n Select An Option: ")
        if option == 1:
            documentBackup()
            userInput = True
        elif option == 2:
            pictureBackup()
            userInput = True
        elif option == 3:
            videoBackup()
            userInput = True
        elif option == 4:
            xamppBackup()
            userInput = True
        elif option == 5:
            completeBackup()
            userInput = True
        elif option == 6:
            option = input("Backup Options: \n 1: Counter Strike \n 2: Destiny 2 \n 3: No mans sky  \n 4: Pubg \n ---------------------- \n Select An Option: ")
            if option == 1:
                csBackup()
                userInput = True
            elif option == 2:
                d2Backup()
                userInput = True
            elif option == 3:
                nmsBackup()
                userInput = True
            elif option == 4:
                pubgBackup()
                userInput = True
            else:
                print("Invalid input")
                userInput = False
        else:
            print("Invalid input")
            userInput = False


main()