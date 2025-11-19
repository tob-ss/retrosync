import os

#C:\Users\tobao\AppData\Roaming\Dolphin Emulator\Wii\title

path = "/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"

game_type = os.listdir(path)

dolphin_games = []

skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]

#for directory in game type, listdir again to actually get the games


for dir in game_type:
        game_path = f"{path}/{dir}"
        current_game = os.listdir(game_path)
        if current_game == ["00000002"]:
           pass
        else:
            dolphin_games.append(current_game)

print(dolphin_games)

with open('wiitdb.txt', 'r') as file:
     data = file.read()
     print(data)

# create second python script; for ech line, extract first 6 characters. then skip the next three (as they are space and =) then add the rest as a value to the key which is the first 6 characters
# make that a csv
# make it so that it prints out the game names in the directory + its age since last modified
# make the script wakes, whenever theres a change in a file in the folder