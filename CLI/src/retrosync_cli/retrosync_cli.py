import click
import requests
import time

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
    url = "http://37.27.217.84/upload/"
    if all and game:
        raise click.BadParameter((click.style("To upload all game saves, please omit the --game or -g flag.", fg='red')))
    if all == False:
        if click.confirm(f"Please confirm that you would like to upload {game} game save from the following device: {device}"):
            click.echo("Upload Started!")
            n = {"DeviceID": device, "Operation": "Upload", "GameID": game, "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(url, json = n)
    else:
        if click.confirm(f"Please confirm that you would like to upload all game saves from the following device: {device}"):
            click.echo("Upload Started!")
            n = {"DeviceID": device, "Operation": "Upload", "GameID": "ALL", "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(url, json = n)

@cli.command()
@click.option('--device','-d', help='Name of the device you want to download saves to.')
@click.option('--game','-g', help='Name of the game you want to download your saves for.')
@click.option('--all', '-a', is_flag=True, help='Download all game saves to device.')
def download(device, game, all):
    """Choose which game saves you would like to download!"""
    url = "http://37.27.217.84/download/"
    if all and game:
        raise click.BadParameter((click.style("To download all game saves, please omit the --game or -g flag.", fg='red')))
    if all == False:
        if click.confirm(f"Please confirm that you would like to download {game} game save to the following device: {device}"):
            click.echo("Download Started!")
            n = {"DeviceID": device, "Operation": "Download", "GameID": game, "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(url, json = n)
    else:
        if click.confirm(f"Please confirm that you would like to download all game saves to the following device: {device}"):
            click.echo("Download Started!")
            n = {"DeviceID": device, "Operation": "Download", "GameID": "ALL", "Completed": False, "TimeStamp": int(time.time())}
            print(n)
            post_request = requests.post(url, json = n)