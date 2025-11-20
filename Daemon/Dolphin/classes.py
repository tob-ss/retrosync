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