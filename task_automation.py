import pyautogui
import webbrowser
import time
import pandas as pd

# Tempo de espera entre cada comando no pyautogui
pyautogui.PAUSE = 0.5


# abrir navegador
webbrowser.open("chrome")
time.sleep(5)

link = "http://127.0.0.1:8000/logar_usuario/"

pyautogui.write(link)
pyautogui.press("enter")

pyautogui.click(x=887, y=395)
pyautogui.write("administrador")
#time.sleep(3)
pyautogui.press("tab")
pyautogui.write("bandal")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=459, y=234)

# Entrar na Tela de cadastro
pyautogui.click(x=659, y=313)

# Abrir arquivo csv
table = pd.read_csv("dados.csv")
print(table)


for line in table.index:   
    pyautogui.write(str(table.loc[line, "nome"]))
    pyautogui.press("tab")

    pyautogui.write(str(table.loc[line, "e-mail"]))
    pyautogui.press("tab")
    #time.sleep(3)

    pyautogui.write(table.loc[line, "data_nascimento"])
    pyautogui.press("tab")
    #time.sleep(3)

    pyautogui.write(str(table.loc[line, "celular"]))    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab", presses=3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=648, y=312)