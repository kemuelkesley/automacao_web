import customtkinter

def button_callback():
    print("dados enviados")

app = customtkinter.CTk()
app.title("My automation")
app.geometry("400x250")
# app.maxsize(width=400, height=250)
# app.minsize(width=400, height=250)
app.resizable(width=False, height=False)



# Título da Tela de Login
title_label = customtkinter.CTkLabel(app, text="Tela de Login", fg_color="transparent", font=("Arial", 20))
title_label.grid(row=0, column=1, columnspan=2, pady=10)

# Rótulo e Entrada para o Usuário
label_user = customtkinter.CTkLabel(app, text="User:", fg_color="transparent", font=("Arial", 15))
label_user.grid(row=1, column=0, sticky="w", ipadx=10, ipady=10)

entry_user = customtkinter.CTkEntry(app, placeholder_text="Informe o usuário", width=250, height=30)
entry_user.grid(row=1, column=1, padx=10, pady=10)
entry_user_value = entry_user.get()
print(entry_user_value)


# Rótulo e Entrada para a Senha
label_password = customtkinter.CTkLabel(app, text="Password:", fg_color="transparent", font=("Arial", 15))
label_password.grid(row=2, column=0, padx=10, pady=10)

entry_password = customtkinter.CTkEntry(app, placeholder_text="Informe a Senha", show="*", width=250, height=30)
entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# Botão de Envio
button = customtkinter.CTkButton(app, text="Enviar", command=button_callback, width=250, height=30)
button.grid(row=3, column=1, padx=10, pady=10)



app.mainloop()