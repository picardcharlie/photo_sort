"""
Goals, build a script that sorts my photos for me.  I save a lot of memes, I want them seperate than my
photos.

Should be able to use regex to sort them, camera saves all photos in a 

XXXXXXXX_XXXXXX.jpg where all values of X are numbers.

Just move all photos that don't fit that into another folder.
"""

import os
import re
import shutil
from pathlib import Path

# make a directory called memes if there isn't on
cwd = os.getcwd()

if not os.path.exists(cwd + "/memes"):
    print("making meme folder")
    os.makedirs((os.path.join(cwd, "memes")))

else:
    print("meme folder already exists, not creating")


meme_directory = cwd + "/memes"

files_moved = 0

def photo_regex(file_name):
    pattern = re.compile(r"\d\d\d\d\d\d\d\d_\d\d\d\d\d\d\.jpg", re.IGNORECASE)
    return pattern.match(file_name)

def check_picture(file_name, current_directory):
    # to use variable outside of function, use global at start of function
    global files_moved
    if bool(photo_regex(file_name)) == False:
        if file_name == "memes" or file_name == "photo_sort.py" or os.path.isdir(file_name):
            print(f"don't move this {file_name}")
        else:
            shutil.move((current_directory + "/" + file_name), (meme_directory + "/" + file_name))
            files_moved += 1


#print(os.listdir(cwd))
# begin looping through all files inside of cwd.
for file in os.listdir(cwd):

	# if a directory, go inside and send any dankness to memes.
    if 	os.path.isdir(file):
        temp_work_dir = cwd + "/" + file
        for files in os.listdir(temp_work_dir):
            check_picture(files, temp_work_dir)


    # check the name of the file against regex
    # if matches camera photo, ignore and go onto the next
    # else, move file to meme folder
    check_picture(file, cwd)

print(f"Operation complete, {files_moved} dank memes and others sorted out.")
