import os
from colorama import Fore, Style, init, Back, init
init()
files=[]
ext = ""
color = ""
lang = ""
def inpt():
    global ext, color, lang, files
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
    cor=input("\nIs it correct?(y/n): ")
for i in range(0,len(files)):
    os.system(f"py image.py {lang} {color} {files[i]}")
    print(Fore.GREEN + f"{i+1}/{len(files)}({files[i]})" + Style.RESET_ALL)