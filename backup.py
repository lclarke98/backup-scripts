import shutil
import os


def documentBackup():
    print("You selected document backup")
    # docs backup
    doc_SOURCE = "F:\\Documents"
    doc_BACKUP = "Z:\\pcBackup\\doc_Backup"
    # Removes current backup directory
    shutil.rmtree(doc_BACKUP)
    # create a backup directory
    shutil.copytree(doc_SOURCE, doc_BACKUP)
    print (os.listdir(doc_BACKUP))

def pictureBackup():
    print("You selected picture backup")
    #pics backup
    pic_SOURCE = "F:\\Pictures"
    pic_BACKUP = "Z:\\pcBackup\\pic_Backup"
    # Removes current backup directory
    shutil.rmtree(pic_BACKUP)
    # create a backup directory
    shutil.copytree(pic_SOURCE, pic_BACKUP)
    print (os.listdir(pic_BACKUP))

def videoBackup():
    print("You selected video backup")
    #pics backup
    vid_SOURCE = "F:\\Videos"
    vid_BACKUP = "Z:\\pcBackup\\vid_Backup"
    # Removes current backup directory
    shutil.rmtree(vid_BACKUP)
    # create a backup directory
    shutil.copytree(vid_SOURCE, vid_BACKUP)
    print (os.listdir(vid_BACKUP))

def xamppBackup():
    print("You selected xampp backup")
    # Websites backup
    web_SOURCE = "C:\\xampp\\htdocs"
    web_BACKUP = "Z:\\pcBackup\\Website_Backup"
    # Removes current backup directory
    shutil.rmtree(web_BACKUP)
    # create a backup directory
    shutil.copytree(web_SOURCE, web_BACKUP)
    print (os.listdir(web_BACKUP))

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