import os
import requests
import json
import time
import pyfiglet
import sys
from instagrapi import Client
from time import sleep
from keyboard import read_event
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح
his3 = "acchis.json"
if os.path.exists(his3):
    with open(his3, "r") as file:
        acchis = json.load(file)
    username = acchis.get("username")
    password = acchis.get("password")
else:
    username = input(A + " - Enter your username: ")
    password = input(A + " - Enter your password: ")

    acchis = {"username": username, "password": password}
    with open(his3, "w") as file:
        json.dump(acchis, file)

print(Z1 + '-' * 50)
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3 / 5000)


hispr = pyfiglet.figlet_format(" - Bot - iNsTa ")


def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3 / 1000)


j(X + hispr)


def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3 / 5000)


print(Z1 + '-' * 50)
print(Y + ' - Source Code : @Hisoka2i - @tesla1q')
print(Z1 + '-' * 50)
cl = Client()
cl.login(username, password)
my_user_id = cl.user_id_from_username(username)
url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
def gpt(text) -> str:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message': text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return ""


print(F + " - Done Login - Started Bot ✅ ")


def gpt_reply(message, my_user_id, destinataire):
    if message.user_id != int(my_user_id):
        # حقوق هيسوكا
        prompt = message.text
        if prompt is not None and "stop" not in prompt:
            user_id_message = X+" - From Username : " + destinataire +" - message : " + str(prompt)
            print(user_id_message)
            print()
            print(A + " - Obtaining the response from ChatGPT is in progress 🤖🧠 : ")
            response = gpt(prompt)
            if response is not None:
                print(response)
                cl.direct_send(response, [id_destinataire])
                print(X + " - The response has been successfully sent ✅. ")
            else:
                print(Z + " - Response from ChatGPT is None ❌.")
        else:
            print(Z + " - Response from ChatGPT is None ❌.")
    return True 


his = True
try:
    while his:
        invitation = cl.direct_pending_inbox()
        if len(invitation) > 0:
            for conv in invitation:
                destinataires = conv.users
                destinataire = destinataires[0].username
                id_destinataire = cl.user_id_from_username(destinataire)
                messages = cl.direct_messages(conv.id)
                message = messages[0]
                his = gpt_reply(message, my_user_id, destinataire)
                cl.direct_thread_hide(conv.id)
                print(Z + " - The conversation has been delete ♻️ ! ")

        print(A + " - Reading the message… 👁️ ")
        inbox_threads = cl.direct_threads()
        if len(inbox_threads) > 0:
            for last_thread in inbox_threads:
                destinataires = last_thread.users
                destinataire = destinataires[0].username
                id_destinataire = cl.user_id_from_username(destinataire)
                messages = cl.direct_messages(last_thread.id)
                message = messages[0]
                his = gpt_reply(message, my_user_id, destinataire)
                cl.direct_thread_hide(last_thread.id)
                print(Z + " - The conversation has been delete ♻️ ! ")
        else:
            print(B + " - No message Now ! 🔸")

        sleep(10)  # لتجنب حظر الحساب
except Exception as e:
    
    print(Z1+" - An error occurred:", str(e))
finally:
    
    cl.logout()
