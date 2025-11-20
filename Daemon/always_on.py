import os
import time
import Dolphin.metadata as metadata
import Dolphin.classes as classes

dolphin_games = []

get_saves = classes.save_locations(dolphin_games)

get_saves.gamePathArrays()

print(dolphin_games)

def detect_file_changes(file_path, interval=1):
    last_modified = os.path.getmtime(file_path)
    while True:
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            print("File has changed!")
            last_modified = current_modified
            metadata.dolphin_metadata()
        time.sleep(interval)

# Usage
#detect_file_changes("file.txt")

# need to update function so it uses oswalk and checks for file changes in the entire folder