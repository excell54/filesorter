# Updated file sorter
import os
import shutil
import time
import random

# Gets the username of the user  
username = os.getenv('username')

# Dictionary containing different extensions for each file type
extensions = {
    "Music":[".m4a",".mp3",".wav",".wma"],
    "Pictures":[".jpg",".png",".ico",".jpeg"],
    "Videos":[".mp4",".webm",".avi",".wmv",".mkv"]
}

def extensionCheck():
    userDirectory = ("C:\\Users\\"+username)
    downloadDirectory = (userDirectory+"\\Downloads")

    downloadFolderContents = os.listdir(downloadDirectory) # Variable holds the default download directory.
    
    for fileName in downloadFolderContents:        
        if ".part" in fileName:     # If the file is not downloaded fully, do not move it, move onto the next file.
            continue

        for index in extensions:     # Go through each file-type inside 'extensions' and look through the list of values.
            for extension in extensions[index]:
                if extension in fileName:
                    try:
                        shutil.move((downloadDirectory+"\\"+fileName), (userDirectory+"\\"+index))  # This file extension was found, move the file.
                    except:
                        shutil.move((downloadDirectory+"\\"+fileName), (userDirectory+"\\"+index+str(random.randint(0,1000000))))  # There is already a file with this name so a new name is created.                      

#Runs the procedure indefinitely every 10 seconds
while True:                       
    extensionCheck()
    time.sleep(10)
