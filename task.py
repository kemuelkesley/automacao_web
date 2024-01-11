import pyautogui
import webbrowser
import time
import pandas as pd

# Orientado a objetos

class Task:
    def __init__(self):
        pyautogui.PAUSE = 1.5
        webbrowser.open("chrome")
        time.sleep(3)

    def open_link(self, link):
        pyautogui.write(link)
        pyautogui.press("enter")    


    def make_login(self):
        pyautogui.click(x=887, y=395)
        pyautogui.write("administrador")
        pyautogui.press("tab")
        pyautogui.write("bandal")
        pyautogui.press("tab")       
        pyautogui.press("enter")
        pyautogui.click(x=402, y=231)
        pyautogui.click(x=659, y=313)
        time.sleep(3)
   
   

    def read_csv(self, csv_file):
        table = pd.read_csv(csv_file)
        print(table)
        return table


    def create_registration(self, csv_file):
        table = self.read_csv(csv_file)
        for line in table.index:                
            pyautogui.write(str(table.loc[line, "nome"]))
            pyautogui.press("tab")
            
            pyautogui.write(str(table.loc[line, "e-mail"]))
            pyautogui.press("tab")
            
            pyautogui.write(table.loc[line, "data_nascimento"])
            pyautogui.press("tab")

            pyautogui.write(str(table.loc[line, "celular"]))    
            pyautogui.press("tab")
            pyautogui.press("enter")
            pyautogui.press("tab", presses=3)   
            pyautogui.press("enter")
            time.sleep(3)
            pyautogui.click(x=648, y=312)