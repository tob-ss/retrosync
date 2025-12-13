import os
from dotenv import load_dotenv

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
                    #print(f"looking at {game}")
                    dolphin_games = []
                    dolphin_games.append(game)
                    helper_functions.hex_converter(dolphin_games, game_list_raw, self.game_id_time)
                    converted_ID = helper_functions.simple_hex_convert(game)
                    #print(f"obtained game id: {converted_ID}")
                    #for data in self.game_id_time:
                        #print(f"on current game which is {data['Game Name']}")
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
                                    #print(f"{n} is bigger than {mod_time}, keeping {n}")
                                    pass
                                else:
                                    #print(f"{n} is smaller than {mod_time}, removing {n}")
                                    time_comparison.remove(n)
                                    time_comparison.append(mod_time)
                                    
                                    #print(time_comparison)
                    for t in time_comparison:
                        for entry in self.game_id_time:
                            #print(f"This is the game ID we're comparing {converted_ID}")
                            if entry["GameID"] == converted_ID:
                                entry.update({"LastModified": t})

                                #print(f"added {t} to {entry}")
                            else:
                                pass


        return self.game_id_time


class always_on_functions:
    def __init__(self, file_number_list=[], modified_date_list=[], save_path="/mnt/c/Users/tobao/AppData/Roaming/Dolphin Emulator/Wii/title"):
        self.save_path = save_path
        self.file_number_list = file_number_list
        self.modified_date_list = modified_date_list
    
    def get_total_files(self):
        skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]
        game_type = os.listdir(self.save_path)
        for dir in game_type:
            game_paths = f"{self.save_path}/{dir}"
            current_games = os.listdir(game_paths)
            if current_games == ["00000002"]:
                pass
            else:
                for game in current_games:
                    game_dir = f"{self.save_path}/{dir}/{game}"
                    for path, folders, files in os.walk(game_dir):
                        for save_data in files:
                            
                            self.file_number_list.append(save_data)

    def get_modified_dates(self):
        skip_game_type = ["00000001","00000002", "00010000", "00010001", "00010002", "00010003", "00010004", "00010005", "00010006", "00010007", "00010008"]
        game_type = os.listdir(self.save_path)
        for dir in game_type:
            game_paths = f"{self.save_path}/{dir}"
            current_games = os.listdir(game_paths)
            if current_games == ["00000002"]:
                pass
            else:
                for game in current_games:
                    game_dir = f"{self.save_path}/{dir}/{game}"
                    for path, folders, files in os.walk(game_dir):
                        for save_data in files:
                            mod_time = os.path.getmtime(f"{path}/{save_data}")
                            self.modified_date_list.append(mod_time)     

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

class sync_handler:
    def __init__(self, syncrequest_data, save_path, bucket):
        self.syncrequest_data = syncrequest_data
        self.save_path = save_path
        self.bucket = bucket

    def upload_file_to_b2(file_name, bucket, object_name=None):
        if object_name is None:
            object_name = file_name

        load_dotenv()

        KEY_ID = os.getenv("aws_access_key_id")
        ACCESS_KEY = os.getenv("aws_secret_access_key")

        b2_client = boto3.client('s3')


        try:
            response = b2_client.upload_file(file_name, bucket, object_name)
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        return True

    def upload_folder_to_b2(self):
        for root, dirs, files in os.walk(self.save_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, self.save_path)
                b2_object_name = relative_path.replace("\\", "/")

                print(f"Uploading {local_path} to {self.bucket}/{b2_object_name}")
                success = self.upload_file_to_b2(local_path, self.bucket, b2_object_name)

                if success:
                    print(f"Upload successful: {local_path} has been uploaded to {self.bucket}.")
                else:
                    print("Upload failed")
                
# unfinished, will need to 