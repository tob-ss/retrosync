import requests

class DaemonStatusChecker:
    def __init__(self, DeviceID: str):
        self.DeviceID = DeviceID
        
    def check_status(self):
        get_url = "http://37.27.217.84//daemon/status/"
        x = {"DeviceID": self.DeviceID}
        get_status = requests.get(get_url, params=x)
        return get_status.text
    
    def continue_or_cancel(self):
        response = self.check_status()
        if response == f"{self.DeviceID} is Online":
            return 1
        if response == f"{self.DeviceID} is Offline":
            return 0