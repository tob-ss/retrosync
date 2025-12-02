import os
import time
import classes as classes
import metadata
import requests

#def detect_file_changes(file_path, interval=1):
#    last_modified = os.path.getmtime(file_path)
#    while True:
#        current_modified = os.path.getmtime(file_path)
#        if current_modified != last_modified:
#            print("File has changed!")
#            last_modified = current_modified
#            metadata.dolphin_metadata()
#        time.sleep(interval)

# Usage
#detect_file_changes("file.txt")

x = 0

old_list_file_number_check = []

old_list_modified_date = []

add_metadata = "http://37.27.217.84/metadata/append/"
flush_local = "http://37.27.217.84/metadata/delete/localflush/"
daemonstatus_url = "http://37.27.217.84//daemon/status/"

daemonstatus_dict = {"DeviceID": "Test Device"}

current_time = time.time()

daemonstatus_dict.update({"LastOnline": current_time})

requests.post(daemonstatus_url, json = daemonstatus_dict)

while True:

    start_time = time.time()
    delay = 60

    while time.time() - start_time < delay:
        trigger_metadata = 0

        #new_list_file_number_check = []

        #get_total_files = classes.always_on_functions(file_number_list=new_list_file_number_check)

        #get_total_files.get_total_files()

        #if len(new_list_file_number_check) != len(old_list_file_number_check):
            #print("triggering metadata.py")
            #trigger_metadata = 1
        #else:
            #print("they are the same, moving on")
            #pass

        #old_list_file_number_check = new_list_file_number_check

        new_list_modified_date = []

        get_modified_dates = classes.always_on_functions(modified_date_list=new_list_modified_date)

        get_modified_dates.get_modified_dates()

        #print(sum(new_list_modified_date))

        if sum(new_list_modified_date) != sum(old_list_modified_date):
            #print("triggering metadata.py")
            trigger_metadata = 1
        else:
            #print("they are the same, moving on")
            pass

        old_list_modified_date = new_list_modified_date

        x = 0

        if trigger_metadata == 1:
            metadata.dolphin_metadata()
            DeviceID_local = {}
            DeviceID_local.update({"DeviceID": "Test Device"})
            print(DeviceID_local)
            if x == 1:
                flush_localmetata = requests.post(flush_local, params=DeviceID_local)
                print(flush_localmetata)
            for n in metadata.dolphin_metadata():
                if x == 0:
                    n.update({"LID": "CL"})
                    n.update({"Cloud": "Yes"})
                else:
                    n.update({"LID": "L"})
                    n.update({"Cloud": "No"})
                n.update({"DeviceID": "Test Device"})
                post_request = requests.post(add_metadata, json = n)
                print(post_request.text)
        else:
            pass
        pass

    daemonstatus_dict = {"DeviceID": "Test Device"}

    current_time = time.time()

    daemonstatus_dict.update({"LastOnline": current_time})

    print(daemonstatus_dict)

    requests.post(daemonstatus_url, json = daemonstatus_dict)

   

    



# classes modified date function

# get sum of all modified dates, if new_list sum != old_list sum, trigger metadata.py and old_list = new_list
# else, pass

# 

# need to update function so it uses oswalk and checks for file changes in the entire folder

# when got the classes for checking num of items in folder + time mod
# have some sort of new list at start of loop, and then class functions,
# then do comparisons of new list to an old list
# for num of items in folder, compare num of items in list new to old
# for time mod, compare sum of time mod 
# if is same, leave old same
# if is diff update old with new