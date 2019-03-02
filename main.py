import psutil
from pypresence import Presence
import time
import json
import os
import sys


print("====== Discord Presence Boot Manager ======")
print("         ==== Selection  Menu ====\n         = Start - start app     =\n         =                       =\n         = Exit - exit from app  =\n         =         v1.0          =\n         =========================")
selection = input(">Select option from list: ")
if selection == "Start":
	while True:
		Get_Id = input("\n>Give me client id: ")
		Get_Icon = input("\n>Enter the name of the icon: ")
		Get_Small_Icon = input("\n>Enter small icon name: ")
		Get_Text = input("\n>Enter text: ")
		Get_Text_2 = input("\n>Enter description text: ")
		RPC = Presence(client_id=Get_Id,pipe=0)
		RPC.connect()
		RPC.update(details=""+str(Get_Text), state=""+str(Get_Text_2), large_image=""+str(Get_Icon), small_image=""+str(Get_Small_Icon))
		print("\n[Info] - Presence now running...")
		exit = input("\n>Exit? (y): ")
		if exit == "y":
			sys.exit()
else:
	sys.exit()

