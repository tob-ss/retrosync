import os
import codecs
#C:\Users\tobao\AppData\Roaming\Dolphin Emulator\Wii\title

path = "/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"

game_type = os.listdir(path)

dolphin_games = []

skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]

#for directory in game type, listdir again to actually get the games


for dir in game_type:
        game_paths = f"{path}/{dir}"
        current_games = os.listdir(game_paths)
        if current_games == ["00000002"]:
           pass
        else:
            for game in current_games:
               dolphin_games.append(game)

for hex in dolphin_games:
   hex_str = hex
   res = codecs.decode(hex_str, 'hex').decode('utf-8')
   print(res)

#in the loop if is a game; convert into hex
#compare the hex value with game IDs in the processed csv files
#if the value matches, it should take the value from the processed csv files and add it to a dictionary for now
# make it so that it prints out the game names in the directory + its age since last modified
# make the script wakes, whenever theres a change in a file in the folder