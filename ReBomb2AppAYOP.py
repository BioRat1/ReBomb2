
import requests
from requests.sessions import session
from requests.exceptions import ProxyError
import os
import pyfiglet.fonts
import time
import fp.fp as FreeProxy
import sys
import ipaddress

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from fp.fp import FreeProxy

pyfiglet.FigletFont.DEFAULT_FONT_PATH = 'C:\\Users\\Strai\\OneDrive\\Documents\\C_Projects\\Rebomb2AYOP\\build\\ReBomb2App\\pyfiglet\\fonts'

s = session()
fproxy = FreeProxy(country_id=['US','GB','BR','AS','NA']).get()
proxies = {
            'http': fproxy,
             'https': fproxy
        }

def report(): #Otherwise, use one of the free proxy servers

    url_to_report = url
    
    try:
        response = s.post(url_to_report, proxies=proxies)
        while True:
         print(response.text)
         used_proxy = ["Using proxy: \n" + (str(proxies)), "Reported :D",  ]
         print(used_proxy)
         time.sleep(60)     
    except Exception:
        print("Proxy Error: Restarting")    
        pass        
        report()

def Own_Proxy():
    url_to_report = url
    
    
    Own_Proxy2 = input("Welp, enter your proxy here. ex:20.206.106.192:80: ")
    print("Checking to see if the proxy works")
    proxy_string = Own_Proxy2
    your_proxy = {"http": proxy_string, "https": proxy_string}
    
    
    try:
        response1 = s.post(url_to_report, proxies=your_proxy)
        
        while True:
         print(response1.text)
         used_proxy = ["Using proxy: \n" + your_proxy, "Reported :D",  ]
         print(used_proxy)
         time.sleep(60)
            

    except Exception:
            print("Proxy not working. Using one of ours")
            report()
            
my_banner = pyfiglet.figlet_format("Robomb2")
print(my_banner)
url = input("Insert the Inspect Element URL here: ")
Own_Proxy_input = input("Would you like to add your own proxy? Type 'yes' or 'no': ").lower()
if Own_Proxy_input == "no":
    report()
else:
    Own_Proxy()





       


    
    



            
                 
            


   
   




    



