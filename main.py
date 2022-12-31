import urllib.parse
import sys
import base64
import webbrowser
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tkinter.filedialog import askopenfilename
import time
import os
from win10toast import ToastNotifier
import easygui
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import datetime

# Get the current date and time
now = datetime.datetime.now()
# Use the datetime.strftime method to specify the format of the date and time
date_time = now.strftime("Date %d-%m-%y Time %H-%M-%S")
toaster = ToastNotifier()
COLORSV = ''
BACKGROUND = "true"
DARK_MODE = "true"
PADDING = "64"
LANGUAGEV = ''
#TITLE = str(int(time.time())) + "(" + file_path[file_path.rfind('\\')+1:file_path.find('.')] + ")"
TITLEV=date_time
CODE=''
# Create the root windo
url=''
def get_img():
    url = f"https://ray.so/?colors={COLORSV}&background={BACKGROUND}&darkMode={DARK_MODE}&padding={PADDING}&title={TITLEV}&code={CODE}&language={LANGUAGEV}"
    #webbrowser.open(url)
    try:
        from selenium import webdriver

        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("prefs", {"download.default_directory": "D:\\ВНТУ\\Requests\\img"})
        #edge_options.add_argument("--headless")
        driver = webdriver.Edge(options=edge_options)
        driver.get(url)
        button_export = '//div[@class="setting export"]//button'
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_export)))
        driver.find_element(By.XPATH, button_export).click()
        time.sleep(2)
        os.chdir("D:\\ВНТУ\\Requests\\img")
        from io import BytesIO
        import win32clipboard
        from PIL import Image

        def send_to_clipboard(clip_type, data):
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(clip_type, data)
            win32clipboard.CloseClipboard()

        filepath = f'{TITLEV}.png'
        image = Image.open(filepath)

        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        send_to_clipboard(win32clipboard.CF_DIB, data)
        
        toaster.show_toast("Succses","Your image has been copied!")
        filepath = 'D:\\ВНТУ\\Requests\\img\\' + filepath
    except Exception as e:
        toaster.show_toast("Error","Opos somthing went wrong...\n" + e)
        print(e)
    #webbrowser.open(url)
def brow():
    global file_path
    global contents
    file_path = filedialog.askopenfilename()
    text_entry.delete(0, "end")
    text_entry.insert(INSERT, file_path)
    text_entry.configure(state=tk.NORMAL)
    if file_path.find(".py")!=-1:
        language_var.set(languages[2])
        LANGUAGEV = languages[2]
    elif file_path.find(".cpp")!=-1 or file_path.find(".c")!=-1:
        language_var.set(languages[1])
        LANGUAGEV = languages[1]
    else:
        language_var.set(languages[0])
        LANGUAGEV = languages[0]
    with open(file_path, 'r') as f:
        contents = f.read()
def prints():
    global COLORSV
    global LANGUAGEV
    global TITLEV
    global CODE
    COLORSV = color_var.get()
    BACKGROUND = "true"
    DARK_MODE = "true"
    PADDING = "64"
    LANGUAGEV = language_var.get()
    #TITLE = str(int(time.time())) + "(" + file_path[file_path.rfind('\\')+1:file_path.find('.')] + ")"
    with open(file_path, 'r') as f:
        contents=f.read()

    CODE = base64.b64encode(contents.encode("utf-8")).decode("utf-8")
    CODE = CODE.replace("+", "%2B")
    root.destroy()
    get_img()
root = tk.Tk()
root.title("Choose option")
root.geometry("650x50")
# Create the choose box for language
languages = ["auto", "cpp", "python", "js", "html", "js", "html"]
language_var = tk.StringVar(root)
language_var.set(languages[0])  # Set the default option
language_dropdown = tk.OptionMenu(root, language_var, *languages)
language_dropdown.grid(row=0, column=0)

# Create the choose box for color
colors = ["meadow","breeze", "candy", "crimson", "midnight", "raindrop", "sunset"]
colors.sort()
color_var = tk.StringVar(root)
color_var.set(colors[0])  # Set the default option
color_dropdown = tk.OptionMenu(root, color_var, *colors)
color_dropdown.grid(row=0, column=1)
#text_entry = tk.Entry(root)
#text_entry.grid(row=0, column=2, pady=10)
text_entry = tk.Entry(root, width=53)

# Place the text box in the root window
text_entry.grid(row=0, column=2)
Button(text ="browse", command = brow).grid(row=0, column=4, pady=10, padx=5)
Button(text ="Ok", command = prints).grid(row=0, column=5, pady=10, padx=5)
file_path = filedialog.askopenfilename()
text_entry.insert(INSERT, file_path)
text_entry.configure(state=tk.NORMAL)
if file_path.find(".py")!=-1:
    language_var.set(languages[2])
    LANGUAGEV = languages[2]
elif file_path.find(".cpp")!=-1 or file_path.find(".c")!=-1:
    language_var.set(languages[1])
    LANGUAGEV = languages[1]
else:
    language_var.set(languages[0])
    LANGUAGEV = languages[0]
root.mainloop()
with open(file_path, 'r') as f:
    contents = f.read()

#print(url)

