import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automação Web")
        self.geometry("400x205")
        self.resizable(width=False, height=False)


        