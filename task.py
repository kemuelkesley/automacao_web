import pyautogui
import webbrowser
import time
import pandas as pd

# Orientado a objetos

class Task:
    def __init__(self):        
        pyautogui.PAUSE = 1.5   
        self.user = None
        self.password = None
   

    def user_data(self):
        try:
            self.user = str(input("Digite o usuário: "))            
        except ValueError:
            print("Erro ao digitar os dados")
       

    def user_password(self):
        self.password = str(input("Digite a senha: "))
       

    def open_browser(self):
        webbrowser.open("chrome")


    def open_link(self, link):  
        time.sleep(5)      
        pyautogui.write(link)
        pyautogui.press("enter")    


    def make_login(self):        
        pyautogui.click(x=887, y=395)
        pyautogui.write(str(self.user))
        pyautogui.press("tab")
        pyautogui.write(str(self.password))
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