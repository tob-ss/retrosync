import os

class save_locations:
    def __init__(self, dolphin_games, save_path="/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"):
        self.save_path = save_path
        self.dolphin_games = dolphin_games

    def gamePathArrays(self):
        #print(f"the save path is {self.save_path} and the array should be empty: {self.dolphin_games}")
        skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]
        game_type = os.listdir(self.save_path)
        for dir in game_type:
            game_paths = f"{self.save_path}/{dir}"
            current_games = os.listdir(game_paths)
            if current_games == ["00000002"]:
                pass
            else:
                for game in current_games:
                    self.dolphin_games.append(game)

class metadata_grabber:
    def __init__(self, game_id_time, save_path="/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"):
        self.save_path = save_path
        self.game_id_time = game_id_time

    def get_gameID_Name_Time(self):
        import helper_functions
        game_type = os.listdir(self.save_path)
        game_list_raw = []
        process = wiitdb_processor(game_list_raw)
        process.process_wiitdb()
        for dir in game_type:
            game_paths = f"{self.save_path}/{dir}"
            current_games = os.listdir(game_paths)
            if current_games == ["00000002"]:
                pass
            else:
                for game in current_games:
                    dolphin_games = []
                    dolphin_games.append(game)
                    helper_functions.hex_converter(dolphin_games, game_list_raw, self.game_id_time)
                    #for data in self.game_id_time:
                    #    print(f"on current game which is {data['Game Name']}")
                    #print(game_id_time)
                    game_dir = f"{self.save_path}/{dir}/{game}"
                    #print(game_dir)
                    time_comparison = [0]
                    for path, folders, files in os.walk(game_dir):
                        for save_data in files:
                            
                            mod_time = os.path.getmtime(f"{path}/{save_data}")
                            #print(f"looking at this file {save_data} in the following path: {path} and it has the following modification time: {mod_time}") 
                            for n in time_comparison:
                                if n > mod_time:
                                    #print("passing")
                                    pass
                                else:
                                    print(f"removing {n}")
                                    time_comparison.remove(n)
                                    print(f"adding {mod_time}")
                                    time_comparison.append(mod_time)
                                    
                                    #print(time_comparison)
                    for t in time_comparison:
                        for entry in self.game_id_time:
                            entry.update({"Last Modified": t})
                            print(f"added {t} to {entry}")

        print(self.game_id_time)

class wiitdb_processor:
    def __init__(self, game_list_raw):
        self.game_list_raw = game_list_raw

    def process_wiitdb(self):
        import csv
        with open("csv/wiitdb_processed1.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)  # Create DictReader

            for row in csv_reader:
                self.game_list_raw.append(row)

        with open("csv/wiitdb_processed2.csv", mode="r") as file:
            csv_reader = csv.DictReader(file)  # Create DictReader

            for row in csv_reader:
                self.game_list_raw.append(row)
        
# unfinished, will need to 