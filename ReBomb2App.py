import customtkinter as tk
import requests
from requests.sessions import session
from requests.exceptions import ProxyError
import json
import webbrowser
import os
import sys

#Code created by BioRat

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


s = session()
proxy = FreeProxy(country_id=['US','GB','BR','AS','NA']).get()

proxies = {
    'http': proxy,
    'https': proxy
}

tk.set_appearance_mode("dark")
tk.set_default_color_theme(resource_path("Rembombedit.json"))


root = tk.CTk()
root.geometry("500x500")
root.iconbitmap(resource_path("download.ico"))
root.title("Rebomb2")

url = ""

def open_paypal():
    webbrowser.open_new("https://www.paypal.com/donate/?hosted_button_id=5592N2YS8PAEA")

def text_insert():
    report()
    output = ["Using proxy: \n" + proxy, "Reported :D",  ]
    outputlist = ''
    output.append(outputlist)
    entry2.insert(tk.END, output, "\n")
    return output

def report():
    
    global url
    url_to_report = entry.get(0.0, "end-1c") # get the text from the entry widget
    
    if url_to_report:
        
        url = url_to_report
        
        entry.delete(0.0, tk.END) # delete the text from the entry widget
        try:
            response = s.post(url, proxies=proxies) # use the text as the URL
        
            print(response.text)
        
        except ProxyError:
            errortext = "Proxy Error: restarting"
            entry2.insert(tk.INSERT, errortext)
            pass # handle proxy error if needed
            
    
    root.after(60000, text_insert,)    
   
        


    
frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.CTkLabel(master=frame, text="Rebomb2", font=("Terminal", 24))
label.pack(pady=12, padx=10)

entry = tk.CTkTextbox(root, font=("terminal", 12), bg_color="#000000")
entry.pack(pady=12, padx=10, fill=tk.BOTH, expand=True,)

entry2 = tk.CTkTextbox(root, font=("Terminal", 12))
entry2.pack(pady=12, padx=10, fill=tk.BOTH, expand=True,)

placeholder_text = "Enter the request URL from Inspect Element:"
entry.insert(tk.INSERT, placeholder_text)

def delete_placeholder_text(event):
    if entry.get(0.0, "end-1c") == placeholder_text:
        entry.delete(0.0, tk.END)



entry.bind("<Button-1>", delete_placeholder_text)
entry.bind("<Key>", delete_placeholder_text)



button = tk.CTkButton(master=frame, text="Report", command=text_insert)
button.pack(pady=12, padx=10)
donatebutton = tk.CTkButton(master=frame, text="Donate", command=open_paypal)
donatebutton.pack(pady=12, padx=10)


root.mainloop()
