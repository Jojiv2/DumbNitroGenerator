import random
import webbrowser
import string
import requests
webhook = "your webhook here <3"
print("""
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
                ░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
                ░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
                ░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
                ░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
                ░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
                ░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
                ░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
                ░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
                ░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
                ░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
                ░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
                ░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
                ░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
                ░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
                ░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
                ░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  JOJI - DZ

                https://discord.gg/sF5yKtnhbx
""")
webbrowser.open('https://discord.gg/sF5yKtnhbx')
while True:
    try:
        code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
        post = {"content":"https://discord.com/billing/promotions/"+code}
        head = {

                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                'content-type' : 'application/json'
            }
        s = requests.post(webhook, json=post, headers=head)
    except:
        print("Error... something went wrong")
        break
