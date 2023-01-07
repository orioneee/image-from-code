import os
from colorama import Fore, Style, init, Back, init
import tkinter as tk
from tkinter import filedialog
init()
folder_path=''
files=[]
ext = ""
color = ""
lang = ""
mp=os.getcwd()
def inpt():
    global ext, color, lang, files, folder_path
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    os.chdir(folder_path)
    files.clear()
    ext = input("Enter a file type(.js/.cpp): ")
    color = input("Enter a color: ")
    lang = input("Enter a language: ")

    fileList = os.listdir()
    for fileName in fileList:
        if fileName.find(ext)!=-1:
            files.append(fileName)
cor='n'
while cor!='y':
    inpt()
    print("Aviable files: \n")
    for fileName in files:
        print(fileName)
    print("\nCustomization: ")
    print(f"Extention: {ext}")
    print(f"Color: {color}")
    print(f"Language: {lang}")
    cor=input("\nIs it correct?(y/n): ")
os.chdir(mp)
for i in range(0,len(files)):
    os.system(f"py image.py {lang} {color} {files[i]} {folder_path}")
    print(Fore.GREEN + f"{i+1}/{len(files)}({files[i]})" + Style.RESET_ALL)
