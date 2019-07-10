import shutil
import os

# Websites backup
web_SOURCE = "C:\\xampp\\htdocs"
web_BACKUP = "Z:\\pcBackup\\Website_Backup"
# Removes current backup directory
shutil.rmtree(web_BACKUP)
# create a backup directory
shutil.copytree(web_SOURCE, web_BACKUP)
print (os.listdir(web_BACKUP))


# docs backup
doc_SOURCE = "F:\\Documents"
doc_BACKUP = "Z:\\pcBackup\\doc_Backup"
# Removes current backup directory
shutil.rmtree(doc_BACKUP)
# create a backup directory
shutil.copytree(doc_SOURCE, doc_BACKUP)
print (os.listdir(doc_BACKUP))

#pics backup
pic_SOURCE = "F:\Pictures\Screenshots"
pic_BACKUP = "Z:\\pcBackup\\pic_Backup"
# Removes current backup directory
shutil.rmtree(pic_BACKUP)
# create a backup directory
shutil.copytree(pic_SOURCE, pic_BACKUP)
print (os.listdir(pic_BACKUP))


#shuts pc down once backup completed
os.system("shutdown -s -t 0")
