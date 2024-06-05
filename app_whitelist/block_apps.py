import psutil
import os
import time

def read_blacklist():
    try:
        with open("whitelist.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def block_blacklisted_apps():
    blacklist = read_blacklist()
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            #print(process)
            process_name = process.info['name']
            if process_name.lower() not in [app.lower() for app in blacklist]:
                print(f"Blocking process: {process_name} (PID: {process.info['pid']})")
                process.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def main():
    while True:
        block_blacklisted_apps()
        print("Checking for apps...")
        time.sleep(10)  # Check and block every 10 seconds

main()
