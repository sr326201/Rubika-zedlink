from arsein import Messenger
from arsein.Zedcontent import Antiadvertisement

tabligh = Antiadvertisement("bhnykisnuiepilbkuzlsrfhaillhusca")

bot = Messenger("bhnykisnuiepilbkuzlsrfhaillhusca")

guid_gap = "g0C6pam04be097b204f957d1560289d2"

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
