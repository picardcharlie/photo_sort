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

def photo_regex(file_name):
    pattern = re.compile(r"\d\d\d\d\d\d\d\d_\d\d\d\d\d\d\.jpg", re.IGNORECASE)
    return pattern.match(file_name)

<<<<<<< HEAD
=======
files_moved = 0

>>>>>>> 5a5dab6 (added total operations done)
#print(os.listdir(cwd))
# begin looping through all files inside of cwd.
for file in os.listdir(cwd):

    # keep track of how many files are moved (future update).

    # check the name of the file against regex
    # if matches camera photo, ignore and go onto the next
    # else, move file to meme folder
    if bool(photo_regex(file)) == False:
        if file == "memes" or file == "photo_sort.py":
            print(f"don't move this {file}")
        else:
            shutil.move((cwd + "/" + file), (cwd + "/memes/" + file))
<<<<<<< HEAD
=======
            files_moved += 1

print(f"Operation complete, {files_moved} dank memes and others sorted out.")
>>>>>>> 5a5dab6 (added total operations done)

