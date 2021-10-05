import os
import time
import sys
import requests
from termcolor import colored
from colorama import Fore, Back, Style, init

'''
Black: \u001b[30m
Red: \u001b[31m
Green: \u001b[32m
Yellow: \u001b[33m
Blue: \u001b[34m
Magenta: \u001b[35m
Cyan: \u001b[36m
White: \u001b[37m
Reset: \u001b[0m
'''

class coronalData:


    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key


    def picture():
        print('''\n\u001b[34m

                                             ```.....-.....```
                                         ``..........-....-.....``                \u001b[37m`.\u001b[34m
                                       `............-.-..-:........``           \u001b[37m`--
                                    `.......\u001b[37m----\u001b[34m.:-.-.-...............`       \u001b[37m`-/-
                                   `.....\u001b[37m./+/::///:\u001b[34m-..-...-............`   \u001b[37m`.://.
                                  .......\u001b[37m-s---.-.-://:\u001b[34m-...-...............\u001b[37m:/+/-`
                                `.........\u001b[37m+..-.-....-/+:\u001b[34m-...........--\u001b[37m://++/-`
                                .........-\u001b[37ms............:+:\u001b[34m-.....--\u001b[37m://++++/:`
                               ...........\u001b[37mo:............./o:\u001b[34m-\u001b[37m://+++/////.\u001b[34m...
                              `...\u001b[31m++++  :+/    ++++     :+sdyoo/    oso\u001b[34m-....`
                              `...\u001b[31m+MMMy  M:   .mMMMd    dMNoo      mMMMs\u001b[34m....`
                              ....\u001b[31m+NmMMd:M:   oNyMMMy   mMMNh     sdsMMM \u001b[34m....
                              ....\u001b[31m+N-hMMNM:  :mds MMM      hhmMd  Nhs MMN\u001b[34m-...
                              `..-\u001b[31m+N   MMM:  oNo   MMm  oysohMm/ hm:   MMh   \u001b[34m
                             `.::-::-..:::-.-::-:\u001b[37ms+:/+/-/:/+/:-.-o:..-::::-.`
                             \u001b[34m``..................\u001b[37m:os+-...........//.--.:....
                                \u001b[34m.............--\u001b[37m:::-\u001b[37m:yh/........-.:+....-:..
                                \u001b[34m ...-.--..--\u001b[37m:/:-....\u001b[37m-:-........-.:+..-....`
                                  \u001b[34m....--.-\u001b[37m::----........\u001b[37m--.----::+\u001b[34m-..:-..
                                   `...-\u001b[37m::-\u001b[34m.-..-....-........----......`
                                    `\u001b[37m-:-\u001b[34m....-:..................-....`
                                  `..\u001b[37m` `\u001b[34m.....-.....................`
                                  \u001b[37m.`\u001b[34m      ``....................`
                                              ````.......````

        \u001b[0m''')


    def coronal_introduction():
        print(u"\u001b[34m\nCORONAL MASS EJECTION DATA ANALYZER\n\u001b[0m")
        print("A coronal mass ejection is a significant release of plasma and accompanying magnetic field from the solar corona.")
        print("They often follow solar flares and are normally present during a solar prominence eruption.")
        print("The plasma is released into the solar wind, and can be observed in coronagraph imagery.")
        print("\n")
        print("The Large Angle and Spectrometric coronagraph (LASCO) instrument is one of eleven instruments included on the joint NASA/ESA Solar and Heliospheric Observatory spacecraft.")
        print("This instrument uses a laser array which measure these solar ejections.")
        print("\n")


    def get_coronal_data():
        response = requests.get(f"https://api.nasa.gov/DONKI/CME?startDate={start_time_year}-{start_time_month}-{start_time_day}&endDate={end_time_year}-{end_time_month}-{end_time_day}&api_key={api_key}")
        time_start = time.perf_counter()
        query = response.json()

        for x in query:
            print(u"\u001b[31m[*] EVENT: " + x['activityID'] + "\u001b[0m")
            print(u"[*] REGION: " + str(x['activeRegionNum']) + "\u001b[0m")
            print(u"[*] SOURCE LOCATION: " + x['sourceLocation'] + "\u001b[0m")
            print(u"\u001b[36m[*] NOTE: " + x['note'] + "\u001b[0m")
            laser_device_name = x['instruments'][0]['displayName']
            print(u"[*] EQUIPMENT NAME: " + laser_device_name)
            speed = x['cmeAnalyses'][0]['speed']
            print(u"\u001b[33m[*] SPEED: " + str(speed) + "\u001b[0m")
            print("\n")

        time_end = time.perf_counter()
        print(f"Completed task in: {time_end - time_start:0.4f} seconds")


if __name__ == '__main__':

    username = "collinsullivan@protonmail.com"
    api_key = "7OjWaZYLcYzdRFGF73x9n9OBHpkMFcyaiUy6c0fH"

    init()
    query_data = coronalData(username, api_key)
    coronalData.picture()
    coronalData.coronal_introduction()

    start_time_year = input("[-] Please enter a start year: ")
    start_time_month = input("[-] Please enter a start month: ")
    start_time_day = input("[-] Please enter a start date: ")
    end_time_year = input("[-] Please enter an end year: ")
    end_time_month = input("[-] Please enter an end month: ")
    end_time_day = input("[-] Please enter an end date: ")
    print("\n")
    coronalData.get_coronal_data()
