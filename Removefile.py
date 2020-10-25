import os
import shutil
import time

def Removefiles():
    path ="pathToDelete"
    numberOfFoldersCount = 0
    numberOfFilesCount = 0
    days = 60
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for folders,files in os.walk(path):
            if seconds>= age(folders,files):
                numberOfDeletedFolders = numberOfDeletedFolders +1
            else:
                numberOfDeletedFolders = 0
    print("numberOfDeletedFolders")
Removefiles()