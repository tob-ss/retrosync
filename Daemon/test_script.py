import os
import codecs
import csv
import time
#C:\Users\tobao\AppData\Roaming\Dolphin Emulator\Wii\title

save_path = "/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"

game_type = os.listdir(save_path)

dolphin_games = []

skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]

#for directory in game type, listdir again to actually get the games


for dir in game_type:
        game_paths = f"{save_path}/{dir}"
        current_games = os.listdir(game_paths)
        if current_games == ["00000002"]:
           pass
        else:
            for game in current_games:
               dolphin_games.append(game)

with open("csv/wiitdb_processed1.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    game_list_raw = []  # List to store dictionaries
    for row in csv_reader:
        game_list_raw.append(row)

with open("csv/wiitdb_processed2.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)  # Create DictReader

    for row in csv_reader:
        game_list_raw.append(row)

game_list_processed = []

for hex in dolphin_games:
   hex_str = hex
   res = codecs.decode(hex_str, 'hex').decode('utf-8')
   duplicate = []
   for data in game_list_raw:
       if res == data["Game ID"] and res not in duplicate:
         duplicate.append(res)
         #print(f"Game ID is {res} and Game Name is {data['Game Name']}")
         game_list_processed.append({"Game ID": res, "Game Name": data['Game Name']})

print(game_list_processed)

for dir in game_type:
   game_paths = f"{save_path}/{dir}"
   current_games = os.listdir(game_paths)
   if current_games == ["00000002"]:
      pass
   else:
      for game in current_games:
         print(f"on current game which is {game}")
         game_dir = f"{save_path}/{dir}/{game}"
         time_comparison = [0]
         for path, folders, files in os.walk(game_dir):
            for save_data in files: 
               mod_time = os.path.getmtime(f"{path}/{save_data}")
               for n in time_comparison:
                  if n > mod_time:
                      print("passing")
                  else:
                     time_comparison.append(mod_time)
                     time_comparison.remove(n)
         print(time_comparison) 

               #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(mod_time))
               #print(formatted_time)
               

# age since modified
# need to figure out a way to get the modification date in same dictionary
# get the modification dates seperately. create a second dict with game ids and modification dates
# need to loop recursively through every file in each folder and get modification date
# the bigger epoch time is the most recent
# then combine the two dictionaries based on game ID
# make the script wakes, whenever theres a change in a file in the folder