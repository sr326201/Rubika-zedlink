import os
os.system("clear")
os.system("pip install colorama")
os.system("pip install ArseinRubika")
from arsein import Messenger
from arsein.Zedcontent import Antiadvertisement
from colorama import *

#os.system("clear")
#os.system("pip install colorama")
#os.system("pip install ArseinRubika")
input = input(Fore.GREEN+"Enter Aothe >>> ")
Goide = input(Fore.RED+"Enter Goid Group >>> ")
Grop = input(Fore.RED+"Link Grop >>> ")
tabligh = Antiadvertisement(input)
bot = Messenger(input)
bot.joinGroup(Grop)
guid_gap = Goide
list_id = []

de = 0

while 1:
	try:
		message = bot.getChatGroup(guid_gap)
		for msg in message:
			if not msg.get("message_id") in list_id:
				list_id.append(msg.get("message_id"))
				tabligh.Anti("link",guid_gap,msg)
				de += 1
				print(de)
	except:continue
