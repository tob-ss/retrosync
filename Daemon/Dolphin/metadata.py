def dolphin_metadata():

   import os
   import codecs
   import csv
   import time
   import Dolphin.helper_functions as helper_functions
   import classes
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

   helper_functions.hex_converter(dolphin_games, game_list_raw, game_list_processed)

   #print(game_list_processed)

   game_id_time = []



   for dir in game_type:
      game_paths = f"{save_path}/{dir}"
      current_games = os.listdir(game_paths)
      if current_games == ["00000002"]:
         pass
      else:
         
         for game in current_games:
            dolphin_games = []
            #print(f"on current game which is {game}")
            dolphin_games.append(game)
            helper_functions.hex_converter(dolphin_games, game_list_raw, game_id_time)
            #print(game_id_time)
            game_dir = f"{save_path}/{dir}/{game}"
            time_comparison = [0]
            for path, folders, files in os.walk(game_dir):
               for save_data in files: 
                  mod_time = os.path.getmtime(f"{path}/{save_data}")
                  for n in time_comparison:
                     if n > mod_time:
                        #print("passing")
                        pass
                     else:
                        time_comparison.remove(n)
                        time_comparison.append(mod_time)
                        
                        #print(time_comparison)
            for t in time_comparison:
               for entry in game_id_time:
                  entry.update({"Last Modified": t})

   print(game_id_time)
            #for time_epoch in time_comparison: 
               #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_epoch))
               #print(formatted_time)
                  


   # make the script wakes, whenever theres a change in a file in the folder
