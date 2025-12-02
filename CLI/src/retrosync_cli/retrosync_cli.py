import click
import requests
import time

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
        print(response)
        if response == f"{self.DeviceID} is Online":
            return 1
        if response == f"{self.DeviceID} is Offline":
            return 0

@click.group()
def cli():
    """Retrosync's CLI for managing your Retro Game Saves!"""
    pass

@cli.command()
@click.option('--device','-d', help='Name of the device you want to upload saves from.')
@click.option('--game','-g', help='Name of the game you want to upload your saves for.')
@click.option('--all', '-a', is_flag=True, help='Upload all game saves on device.')
def upload(device, game, all):
    """Choose which game saves you would like to upload!"""
    sync_url = "http://37.27.217.84//sync/append/"
    
    if all and game:
        raise click.BadParameter((click.style("To upload all game saves, please omit the --game or -g flag.", fg='red')))
    if all == False:
        if click.confirm(f"Please confirm that you would like to upload {game} game save from the following device: {device}"):
            click.echo(f"Checking if device {device} is online...")
            status = DaemonStatusChecker(device)
            if status.continue_or_cancel() == 1:
                click.echo("Upload Started!")
                n = {"DeviceID": device, "Operation": "Upload", "GameID": game, "Completed": False, "TimeStamp": int(time.time())}
                print(n)
                sync_request = requests.post(sync_url, json = n)
            else:
                click.echo(f"Could not connect to {device}... Please check if Retrosync is running or if device is connected to the internet")
                click.echo(f"Cancelling Upload...")   
    else:
        if click.confirm(f"Please confirm that you would like to upload all game saves from the following device: {device}"):
            click.echo(f"Checking if device {device} is online...")
            status = DaemonStatusChecker(device)
            if status.continue_or_cancel() == 1:
                click.echo(f"{device} is online... Starting Upload!")
                click.echo("Upload Started!")
                n = {"DeviceID": device, "Operation": "Upload", "GameID": "ALL", "Completed": False, "TimeStamp": int(time.time())}
                print(n)
                sync_request = requests.post(sync_url, json = n)
            else:
                click.echo(f"Could not connect to {device}... Please check if Retrosync is running or if device is connected to the internet")
                click.echo(f"Cancelling Upload...")

@cli.command()
@click.option('--device','-d', help='Name of the device you want to download saves to.')
@click.option('--game','-g', help='Name of the game you want to download your saves for.')
@click.option('--all', '-a', is_flag=True, help='Download all game saves to device.')
def download(device, game, all):
    """Choose which game saves you would like to download!"""
    sync_url = "http://37.27.217.84//sync/append/"
    if all and game:
        raise click.BadParameter((click.style("To download all game saves, please omit the --game or -g flag.", fg='red')))
    if all == False:
        if click.confirm(f"Please confirm that you would like to download {game} game save to the following device: {device}"):
            click.echo("Download Started!")
            n = {"DeviceID": device, "Operation": "Download", "GameID": game, "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(sync_url, json = n)
    else:
        if click.confirm(f"Please confirm that you would like to download all game saves to the following device: {device}"):
            click.echo("Download Started!")
            n = {"DeviceID": device, "Operation": "Download", "GameID": "ALL", "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(sync_url, json = n)