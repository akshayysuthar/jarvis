import os
import keyword
import pyautogui
import webbrowser

chrome = f"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
vscode = r"C:\Users\Savita\AppData\Local\Programs\Microsoft VS Code\Code.exe"

def OpenExe(Query):
    Query = str(Query).lower()

    if "open" in Query :
        Name = Query.replace("visit ","")
        Name = Query.replace("open ", "")


        link = f"https://www.{Name}.com"
        webbrowser.open(link)
        return True

    elif "start" in Query:
        Name = Query.replace("open", "")

        if "chrome" in Name:
            os.startfile(chrome)
            return True

        elif "vs code" in Query:
            os.startfile(vscode)
            return True
