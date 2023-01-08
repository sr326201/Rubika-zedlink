import os
os.system("clear")
os.system("pip install colorama")
os.system("pip install ArseinRubika")
from arsein import Messenger
from arsein.Zedcontent import Antiadvertisement
from colorama import *
import time
os.system("clear")

Auth1 = input(Fore.GREEN+"Enter Authe Bot >>> ")
time.sleep(1.5)
Auth = input(Fore.GREEN+"Enter Authe2 Bot >>> ")
time.sleep(1.5)
Test = input(Fore.RED+"Enter Goid Group >>> ")
time.sleep(1)
Grop = input(Fore.RED+"Send me Your Group Link>>> ")

tabligh = Antiadvertisement(Auth1)
bot = Messenger(Auth)
bot.joinGroup(Grop)
guid_gap = Test
list_id = []

de = 0

while True:
	try:
		message = bot.getChatGroup(guid_gap)
		for msg in message:
			if not msg.get("message_id") in list_id:
				list_id.append(msg.get("message_id"))
				tabligh.Anti("link",guid_gap,msg)
				de += 1
				print(de)
	except:continue
