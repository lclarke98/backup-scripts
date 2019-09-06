import shutil
import os

def completeBackup():
    print("You selected video backup")
    #pics backup
    vid_SOURCE = "F:\\Videos"
    vid_BACKUP = "Z:\\pcBackup\\vid_Backup"
    # Removes current backup directory
    shutil.rmtree(vid_BACKUP)
    # create a backup directory
    shutil.copytree(vid_SOURCE, vid_BACKUP)
    print (os.listdir(vid_BACKUP))


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
        option = input("Backup Options: \n 1: Complete \n 2: Counter Strike \n 3: Destiny 2 \n 4: No mans sky \n 5: Pubg \n  ---------------------- \n Select An Option: ")
        if option == 1:
            completeBackup()
            userInput = True
        elif option == 2:
            csBackup()
            userInput = True
        elif option == 3:
            d2Backup()
            userInput = True
        elif option == 4:
            nmsBackup()
            userInput = True
        elif option == 5:
            pubgBackup()
            userInput = True
        else:
            print("Invalid input")
            userInput = False

main()