def dolphin_metadata():

   import os
   import codecs
   import csv
   import time
   import helper_functions
   import classes
   #C:\Users\tobao\AppData\Roaming\Dolphin Emulator\Wii\title

   save_path = "/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"

   game_type = os.listdir(save_path)

   dolphin_games = []

   skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]

   game_list_raw = []

   wiitdb_processor = classes.wiitdb_processor(game_list_raw)

   wiitdb_processor.process_wiitdb()

   game_list_processed = []

   helper_functions.hex_converter(dolphin_games, game_list_raw, game_list_processed)

   #print(game_list_processed)

   game_id_time = []

   get_game_id_time = classes.metadata_grabber(game_id_time)

   get_game_id_time.get_gameID_Name_Time()

            #for time_epoch in time_comparison: 
               #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time_epoch))
               #print(formatted_time)
                  


   # make the script wakes, whenever theres a change in a file in the folder

